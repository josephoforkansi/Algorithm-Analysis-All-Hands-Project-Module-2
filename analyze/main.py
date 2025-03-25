"""Main module for queue implementation analysis."""

from typing import Type, Any, Dict, List, Callable
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from time import perf_counter
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

from analyze.DLL import Queue as DLLQueue
from analyze.SLL import LinkedQueue as SLLQueue
from analyze.ListQueue import ListQueueDisplay as ArrayQueue
from analyze.timer import TimingResult
from analyze.queue_approach import QueueApproach

# Create console for rich output
console = Console()

# Create Typer app
app = typer.Typer(
    help="Queue Implementation Performance Analysis Tool",
    add_completion=False,
    no_args_is_help=True,
)

# Map queue implementations to their classes
QUEUE_IMPLEMENTATIONS: Dict[QueueApproach, Type[Any]] = {
    QueueApproach.dll: DLLQueue,
    QueueApproach.sll: SLLQueue,
    QueueApproach.array: ArrayQueue,
}


def time_operation(func: Callable[[], None]) -> float:
    """Time an operation using high-precision counter."""
    start_time = perf_counter()
    try:
        func()
    except Exception as e:
        console.print(f"[red]Error during operation: {str(e)}[/red]")
        return 0.0
    return perf_counter() - start_time


def get_operation_function(operation: str, queue: Any, size: int) -> Callable[[], None]:
    """Get the operation function for timing."""
    if operation == "enqueue":
        return lambda: [queue.enqueue(i) for i in range(size)]
    elif operation == "dequeue":
        return lambda: queue.dequeue()
    elif operation == "peek":
        return lambda: queue.peek()
    elif operation == "concat":
        other = queue.__class__()
        for i in range(size // 10):
            other.enqueue(i)
        return lambda: queue + other
    elif operation == "iconcat":
        other = queue.__class__()
        for i in range(size // 10):
            other.enqueue(i)
        return lambda: queue.__iadd__(other)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def run_doubling_experiment(
    queue_class: Type[Any], initial_size: int, max_size: int, operations: List[str]
) -> Dict[str, List[tuple[int, float]]]:
    """Run doubling experiment on a queue implementation."""
    if initial_size <= 0 or max_size <= 0 or initial_size > max_size:
        raise ValueError("Invalid size parameters")

    results = {}
    size = initial_size

    while size <= max_size:
        for operation in operations:
            if operation not in results:
                results[operation] = []

            total_time = 0
            # Run each operation 10 times and take average
            for _ in range(10):
                queue = queue_class()
                other = None
                try:
                    # Pre-fill queue
                    for i in range(size):
                        queue.enqueue(i)

                    # Get and time the operation
                    op_func = get_operation_function(operation, queue, size)
                    total_time += time_operation(op_func)

                finally:
                    # Clean up to free memory
                    del queue
                    if other is not None:
                        del other

            avg_time = total_time / 10
            results[operation].append((size, avg_time))

        size *= 2

    return results


def plot_results(
    results: Dict[str, List[tuple[int, float]]], queue_type: str, output_dir: Path
):
    """Plot doubling experiment results."""
    plt.figure(figsize=(12, 8))

    for operation, data in results.items():
        sizes, times = zip(*data)
        plt.plot(sizes, times, marker="o", label=operation)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title(f"Doubling Experiment Results - {queue_type}")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")

    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plot_path = output_dir / f"{queue_type.lower()}_doubling_{timestamp}.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path


def run_tests(queue_class: Type[Any], size: int) -> TimingResult:
    """Run performance tests on a queue implementation."""
    if size <= 0:
        raise ValueError("Size must be positive")

    queue = queue_class()

    try:
        # Test enqueue
        enqueue_time = time_operation(lambda: [queue.enqueue(i) for i in range(size)])
        queue.timing_result.add_timing("enqueue", enqueue_time, size)

        # Test dequeue
        dequeue_count = size // 2
        dequeue_time = time_operation(
            lambda: [queue.dequeue() for _ in range(dequeue_count)]
        )
        queue.timing_result.add_timing("dequeue", dequeue_time, dequeue_count)

        # Test peek
        peek_count = size // 3
        peek_time = time_operation(lambda: [queue.peek() for _ in range(peek_count)])
        queue.timing_result.add_timing("peek", peek_time, peek_count)

        # Test length and empty checks
        check_count = size // 4
        check_time = time_operation(
            lambda: [len(queue) or queue.is_empty() for _ in range(check_count)]
        )
        queue.timing_result.add_timing("length/empty", check_time, check_count)

        return queue.timing_result
    finally:
        # Clean up
        del queue


def create_table(result: TimingResult) -> Table:
    """Create a table showing timing information."""
    impl_type = (
        "DLL" if "DLL" in result.name else "SLL" if "SLL" in result.name else "Array"
    )

    table = Table(
        box=box.ROUNDED,
        show_header=True,
        title=f"[bold]{impl_type} Queue Implementation Performance Analysis[/bold]",
    )

    table.add_column("Operation", style="cyan")
    table.add_column("Time (ms)", justify="right", style="green")
    table.add_column("Elements", justify="right", style="yellow")
    table.add_column("Time/Element (ms)", justify="right", style="magenta")

    for op_name, (time, elements) in sorted(result.operations.items()):
        if time > 0 and elements > 0:
            time_ms = time * 1000
            time_per_element_ms = (time / elements) * 1000
            table.add_row(
                op_name,
                f"{time_ms:.6f}",
                f"{elements:,}",
                f"{time_per_element_ms:.6f}",
            )

    return table


def get_selected_approaches(dll: bool, sll: bool, array: bool) -> List[QueueApproach]:
    """Get list of selected queue approaches based on command line options."""
    if not any([dll, sll, array]):
        return list(QueueApproach)
    return [
        app
        for app, flag in [
            (QueueApproach.dll, dll),
            (QueueApproach.sll, sll),
            (QueueApproach.array, array),
        ]
        if flag
    ]


def create_doubling_table(
    results: Dict[str, List[tuple[int, float]]], queue_type: str
) -> Table:
    """Create a table showing doubling experiment results."""
    table = Table(
        box=box.ROUNDED,
        show_header=True,
        title=f"[bold]{queue_type} Queue Doubling Experiment Results[/bold]",
    )

    # Add columns
    table.add_column("Size (n)", style="cyan", justify="right")
    for operation in sorted(results.keys()):
        table.add_column(operation, style="green", justify="right")
    table.add_column("Growth Ratios", style="magenta", justify="right")

    # Get all unique sizes
    sizes = sorted(set(size for op_data in results.values() for size, _ in op_data))

    # Previous times for calculating ratios
    prev_times = {op: 0.0 for op in results.keys()}

    # Add rows for each size
    for size in sizes:
        row = [f"{size:,}"]
        times = []

        # Add times for each operation
        for operation in sorted(results.keys()):
            time = next((t for s, t in results[operation] if s == size), None)
            times.append(time if time is not None else 0.0)
            row.append(f"{time * 1000:.6f}" if time is not None else "N/A")

        # Calculate and add growth ratios
        if size == sizes[0]:
            row.append("Base")
        else:
            # Calculate average ratio compared to previous size
            ratios = []
            for i, time in enumerate(times):
                if prev_times[sorted(results.keys())[i]] > 0 and time > 0:
                    ratio = time / prev_times[sorted(results.keys())[i]]
                    ratios.append(ratio)

            if ratios:
                avg_ratio = sum(ratios) / len(ratios)
                row.append(f"{avg_ratio:.2f}x")
            else:
                row.append("N/A")

        # Update previous times
        for i, op in enumerate(sorted(results.keys())):
            prev_times[op] = times[i]

        table.add_row(*row)

    return table


@app.command()
def analyze(
    size: int = typer.Option(1000, "--size", "-s", help="Size of the data structure"),
    dll: bool = typer.Option(False, "--dll", help="Test DLL Queue implementation"),
    sll: bool = typer.Option(False, "--sll", help="Test SLL Queue implementation"),
    array: bool = typer.Option(
        False, "--array", help="Test Array Queue implementation"
    ),
):
    """Run basic performance analysis on queue implementations."""
    if size <= 0:
        console.print("[red]Error: Size must be positive[/red]")
        return

    for approach in get_selected_approaches(dll, sll, array):
        try:
            result = run_tests(QUEUE_IMPLEMENTATIONS[approach], size)
            console.print(Panel(create_table(result)))
        except Exception as e:
            console.print(f"[red]Error testing {approach.name}: {str(e)}[/red]")


@app.command()
def doubling(
    initial_size: int = typer.Option(
        100, "--initial-size", "-n", help="Initial size for doubling experiment"
    ),
    max_size: int = typer.Option(
        10000, "--max-size", "-m", help="Maximum size for doubling experiment"
    ),
    output_dir: str = typer.Option(
        "results", "--output-dir", "-o", help="Directory to save results"
    ),
    dll: bool = typer.Option(False, "--dll", help="Test DLL Queue implementation"),
    sll: bool = typer.Option(False, "--sll", help="Test SLL Queue implementation"),
    array: bool = typer.Option(
        False, "--array", help="Test Array Queue implementation"
    ),
):
    """Run doubling experiment on queue implementations."""
    if initial_size <= 0 or max_size <= 0 or initial_size > max_size:
        console.print("[red]Error: Invalid size parameters[/red]")
        return

    operations = ["enqueue", "dequeue", "peek", "concat", "iconcat"]
    output_path = Path(output_dir)

    for approach in get_selected_approaches(dll, sll, array):
        queue_class = QUEUE_IMPLEMENTATIONS[approach]
        impl_name = approach.name.upper()

        try:
            results = run_doubling_experiment(
                queue_class, initial_size, max_size, operations
            )
            console.print(Panel(create_doubling_table(results, impl_name)))
            plot_path = plot_results(results, impl_name, output_path)
            console.print(f"Plot saved to: {plot_path}")
        except Exception as e:
            console.print(f"[red]Error testing {impl_name}: {str(e)}[/red]")


if __name__ == "__main__":
    app()

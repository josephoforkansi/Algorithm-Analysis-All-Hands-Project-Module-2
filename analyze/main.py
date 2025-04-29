"""Main module for queue implementations."""

from typing import Type, Any, Dict, List
from enum import Enum
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from time import perf_counter
import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from analyze.dll_queue import Queue as DLLQueue
from analyze.sll_queue import BasicSLLQueue as SLLQueue
from analyze.array_queue import ArrayQueue


class QueueApproach(str, Enum):
    """Enum for different queue implementations."""
    dll = "dll"
    sll = "sll"
    array = "array"


# Map queue implementations to their classes
QUEUE_IMPLEMENTATIONS = {
    QueueApproach.dll: DLLQueue,
    QueueApproach.sll: SLLQueue,
    QueueApproach.array: ArrayQueue,
}

# Create console for rich output
console = Console()

# Create Typer app
app = typer.Typer(
    help="Queue Implementation Performance Analysis Tool",
    add_completion=False,
    no_args_is_help=True,
)


def time_operation(func):
    """Time an operation using high-precision counter."""
    try:
        # Warm up
        func()

        # Actual timing
        start_time = perf_counter()
        func()
        elapsed = perf_counter() - start_time
        return elapsed
    except Exception:
        return float("nan")


def analyze_queue(queue_class, size=1000):
    """Analyze a queue implementation."""
    approach = next((k for k, v in QUEUE_IMPLEMENTATIONS.items() if v == queue_class), None)
    if approach is None:
        console.print("[red]Unknown queue implementation[/red]")
        return

    console.print(f"\n{approach.value.upper()} Queue Implementation")

    try:
        queue = queue_class()
        operations = []

        # Test enqueue
        enqueue_time = time_operation(lambda: [queue.enqueue(i) for i in range(size)])
        operations.append(("enqueue", enqueue_time, size))

        # Test dequeue
        dequeue_count = size // 2
        dequeue_time = time_operation(lambda: [queue.dequeue() for _ in range(dequeue_count)])
        operations.append(("dequeue", dequeue_time, dequeue_count))

        # Refill queue
        for i in range(dequeue_count):
            queue.enqueue(i)

        # Test peek
        peek_count = size // 3
        peek_time = time_operation(lambda: [queue.peek() for _ in range(peek_count)])
        operations.append(("peek", peek_time, peek_count))

        # Test concat
        other = queue_class()
        for i in range(size // 10):
            other.enqueue(i)
        concat_time = time_operation(lambda: queue + other)
        operations.append(("concat", concat_time, size // 10))

        # Test iconcat
        iconcat_time = time_operation(lambda: queue.__iadd__(other))
        operations.append(("iconcat", iconcat_time, size // 10))

        # Test removelast
        removelast_count = size // 4
        removelast_time = time_operation(lambda: [queue.removelast() for _ in range(removelast_count) if queue.size() > 0])
        operations.append(("removelast", removelast_time, removelast_count))

        # Display results in table
        table = Table(
            title=f"{approach.value.upper()} Queue Performance Analysis",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("Operation", style="cyan")
        table.add_column("Time (ms)", justify="right")
        table.add_column("Elements", justify="right")
        table.add_column("Time/Element (ms)", justify="right")

        for operation, time_taken, elements in operations:
            time_per_element = time_taken / elements if elements > 0 else 0
            table.add_row(
                operation,
                f"{time_taken * 1000:.6f}",
                f"{elements:,}",
                f"{time_per_element * 1000:.6f}",
            )

        console.print(Panel(table))

    except Exception as e:
        console.print(f"[red]Error testing {approach.value}: {str(e)}[/red]")
        import traceback
        console.print(traceback.format_exc())


@app.command()
def analyze(
    size: int = typer.Option(1000, help="Size of queue for testing"),
    dll: bool = typer.Option(True, help="Test DLL implementation"),
    sll: bool = typer.Option(True, help="Test SLL implementation"),
    array: bool = typer.Option(True, help="Test Array implementation"),
):
    """Run basic performance analysis on queue implementations."""
    for approach, queue_class in QUEUE_IMPLEMENTATIONS.items():
        if (
            (approach == QueueApproach.dll and dll)
            or (approach == QueueApproach.sll and sll)
            or (approach == QueueApproach.array and array)
        ):
            analyze_queue(queue_class, size)


@app.command()
def doubling(
    initial_size: int = typer.Option(10000, help="Initial size for doubling experiment"),
    max_size: int = typer.Option(1000000, help="Maximum size for doubling experiment"),
    dll: bool = typer.Option(True, help="Test DLL implementation"),
    sll: bool = typer.Option(True, help="Test SLL implementation"),
    array: bool = typer.Option(True, help="Test Array implementation"),
):
    """Run doubling experiment on queue implementations."""
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    sizes = []
    current_size = initial_size
    while current_size <= max_size:
        sizes.append(current_size)
        current_size *= 2

    all_results = {}

    for approach, queue_class in QUEUE_IMPLEMENTATIONS.items():
        if not (
            (approach == QueueApproach.dll and dll)
            or (approach == QueueApproach.sll and sll)
            or (approach == QueueApproach.array and array)
        ):
            continue

        try:
            console.print(f"\n{approach.value.upper()} Queue Implementation")
            results = {op: [] for op in ["enqueue", "dequeue", "peek", "concat", "iconcat", "removelast"]}

            for size in sizes:
                queue = queue_class()
                other = queue_class()

                enqueue_time = time_operation(lambda: [queue.enqueue(i) for i in range(size)])
                results["enqueue"].append(enqueue_time)

                dequeue_time = time_operation(lambda: [queue.dequeue() for _ in range(size // 2)])
                results["dequeue"].append(dequeue_time)

                for i in range(size // 2):
                    queue.enqueue(i)

                peek_time = time_operation(lambda: [queue.peek() for _ in range(size // 3)])
                results["peek"].append(peek_time)

                for i in range(size // 10):
                    other.enqueue(i)

                concat_time = time_operation(lambda: queue + other)
                results["concat"].append(concat_time)

                iconcat_time = time_operation(lambda: queue.__iadd__(other))
                results["iconcat"].append(iconcat_time)

                removelast_time = time_operation(lambda: [queue.removelast() for _ in range(size // 4) if queue.size() > 0])
                results["removelast"].append(removelast_time)

            all_results[approach.value] = results

            table = Table(
                title=f"{approach.value.upper()} Queue Doubling Experiment Results",
                box=box.ROUNDED,
                show_header=True,
                header_style="bold magenta",
                width=85
            )
            table.add_column("Size (n)", justify="right", width=10)
            for op in results.keys():
                table.add_column(f"{op} (ms)", justify="right", width=12)

            for i, size in enumerate(sizes):
                row = [f"{size:,}"]
                for operation in results.keys():
                    value = results[operation][i]
                    row.append(f"{value * 1000:.5f}" if not np.isnan(value) else "N/A")
                table.add_row(*row)

            console.print(Panel(table))

        except Exception as e:
            console.print(f"[red]Error testing {approach.value}: {str(e)}[/red]")
            import traceback
            console.print(traceback.format_exc())

    plot_results(sizes, all_results, results_dir, operations=["enqueue", "dequeue", "peek", "concat", "iconcat", "removelast"])
    console.print(f"[green]Plots saved to [bold]{results_dir}[/bold] directory[/green]")


def plot_results(sizes, all_results, results_dir, operations):
    """Generate and save plots for doubling experiment results."""
    for operation in operations:
        plt.figure(figsize=(10, 6))
        for impl, results in all_results.items():
            times = np.array(results[operation]) * 1000  # to ms
            if not np.all(np.isnan(times)):
                plt.loglog(sizes, times, marker="o", label=f"{impl.upper()}", linewidth=2)

        plt.title(f"{operation.capitalize()} Time Complexity")
        plt.xlabel("Size (n)")
        plt.ylabel("Time (ms)")
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.tight_layout()
        plt.savefig(results_dir / f"{operation}_doubling_experiment.png")
        plt.close()


if __name__ == "__main__":
    app()

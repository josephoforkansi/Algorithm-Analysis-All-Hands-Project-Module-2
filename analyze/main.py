""""Main module for queue implementations."""

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

from analyze.dll_queque import Queue as DLLQueue
from analyze.sll_quque import BasicSLLQueue as SLLQueue
from analyze.ArrayQueue import ArrayQueue


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
    except Exception as e:
        console.print(f"[red]Error during operation: {str(e)}[/red]")
        return float("nan")


def analyze_queue(queue_class, size=1000):
    """Analyze a queue implementation."""
    approach = next(
        (k for k, v in QUEUE_IMPLEMENTATIONS.items() if v == queue_class), None
    )
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
        dequeue_time = time_operation(
            lambda: [queue.dequeue() for _ in range(dequeue_count)]
        )
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
                f"{time_taken * 1000:.6f}",  # Convert to milliseconds
                f"{elements:,}",
                f"{time_per_element * 1000:.6f}",  # Convert to milliseconds
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
    # Create results directory if it doesn't exist
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    sizes = []
    current_size = initial_size
    while current_size <= max_size:
        sizes.append(current_size)
        current_size *= 2

    # Dictionary to store all results for plotting
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
            results = {
                "enqueue": [],
                "dequeue": [],
                "peek": [],
                "concat": [],
                "iconcat": [],
            }

            for size in sizes:
                queue = queue_class()
                other = queue_class()

                # Enqueue
                enqueue_time = time_operation(
                    lambda: [queue.enqueue(i) for i in range(size)]
                )
                results["enqueue"].append(enqueue_time)

                # Dequeue
                dequeue_time = time_operation(
                    lambda: [queue.dequeue() for _ in range(size // 2)]
                )
                results["dequeue"].append(dequeue_time)

                # Refill queue
                for i in range(size // 2):
                    queue.enqueue(i)

                # Peek
                peek_time = time_operation(
                    lambda: [queue.peek() for _ in range(size // 3)]
                )
                results["peek"].append(peek_time)

                # Prepare other queue for concat
                for i in range(size // 10):
                    other.enqueue(i)

                # Concat
                concat_time = time_operation(lambda: queue + other)
                results["concat"].append(concat_time)

                # Iconcat
                iconcat_time = time_operation(lambda: queue.__iadd__(other))
                results["iconcat"].append(iconcat_time)

            # Store results for plotting
            all_results[approach.value] = results

            # Display results in table
            table = Table(
                title=f"{approach.value.upper()} Queue Doubling Experiment Results",
                box=box.ROUNDED,
                show_header=True,
                header_style="bold magenta",
                width=73  # Adjusted table width
            )
            table.add_column("Size (n)", justify="right", width=10)
            table.add_column("enqueue (ms)", justify="right", width=12)
            table.add_column("dequeue (ms)", justify="right", width=12)
            table.add_column("peek (ms)", justify="right", width=12)
            table.add_column("concat (ms)", justify="right", width=12)
            table.add_column("iconcat (ms)", justify="right", width=12)

            for i, size in enumerate(sizes):
                row = [f"{size:,}"]
                for operation in results.keys():
                    value = results[operation][i]
                    if np.isnan(value):  # Check for NaN
                        row.append("N/A")
                    else:
                        row.append(f"{value * 1000:.5f}")  # Show 5 decimal places
                table.add_row(*row)

            console.print(Panel(table))

        except Exception as e:
            console.print(f"[red]Error testing {approach.value}: {str(e)}[/red]")
            import traceback

            console.print(traceback.format_exc())

    # Generate and save plots
    plot_results(sizes, all_results, results_dir, operations=["enqueue", "dequeue", "peek", "concat", "iconcat"])
    console.print(f"[green]Plots saved to [bold]{results_dir}[/bold] directory[/green]")


def plot_results(sizes, all_results, results_dir, operations):
    """Generate and save plots for doubling experiment results."""

    # Create log-log plots for each operation
    for operation in operations:
        if len(sizes) > 2:  # Only create log plots if we have enough data points
            plt.figure(figsize=(10, 6))

            for impl, results in all_results.items():
                times = np.array(results[operation]) * 1000  # Convert to milliseconds
                if np.all(times > 0) and not np.all(np.isnan(times)):  # Avoid log(0) and all NaNs
                    plt.loglog(
                        sizes, times, marker="o", label=f"{impl.upper()}", linewidth=2
                    )

            # Add reference lines for O(1), O(n), O(n²) - only if there's valid data
            valid_data_exists = any(
                not np.all(np.isnan(results[operation])) for results in all_results.values()
            )
            if valid_data_exists and len(sizes) > 1:
                x_range = np.array(sizes)
                # Add O(1) reference (using the first valid time point)
                first_valid_time = next((res[operation][0] * 1000 for res in all_results.values() if not np.isnan(res[operation][0])), None)
                if first_valid_time is not None:
                    plt.loglog(x_range, np.ones_like(x_range) * first_valid_time, "--", label="O(1)", alpha=0.5)
                    # Add O(n) reference - scale to fit
                    plt.loglog(x_range, x_range * (first_valid_time / x_range[0]), "--", label="O(n)", alpha=0.5)
                    # Add O(n²) reference - scale to fit
                    plt.loglog(x_range, np.power(x_range, 2) * (first_valid_time / np.power(x_range[0], 2)), "--", label="O(n²)", alpha=0.5)


            plt.title(
                f"Log-Log Plot for {operation.capitalize()} Operation", fontsize=16
            )
            plt.xlabel("Log Queue Size", fontsize=14)
            plt.ylabel("Log Time (ms)", fontsize=14)
            plt.grid(True, which="both", linestyle="--", alpha=0.5)
            plt.legend(fontsize=12)
            plt.tight_layout()

            # Save log-log plot
            log_plot_path = results_dir / f"{operation}_loglog_plot.png"
            plt.savefig(log_plot_path)
            plt.close()

    # Create regular performance plots for each implementation
    for impl, results in all_results.items():
        plt.figure(figsize=(10, 6))

        for operation in operations:
            times = np.array(results[operation]) * 1000  # Convert to milliseconds
            plt.plot(sizes, times, marker="o", label=operation, linewidth=2)

        plt.title(f"{impl.upper()} Queue Implementation Performance", fontsize=16)
        plt.xlabel("Queue Size (n)", fontsize=14)
        plt.ylabel("Time (ms)", fontsize=14)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend(fontsize=12)
        plt.tight_layout()

        # Save plot
        plot_path = results_dir / f"{impl}_performance.png"
        plt.savefig(plot_path)
        plt.close()


# This is the entry point for Poetry
def main():
    """Entry point for the application."""
    try:
        app()
    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {str(e)}[/red]")
        import traceback

        console.print(traceback.format_exc())


if __name__ == "__main__":
    app()

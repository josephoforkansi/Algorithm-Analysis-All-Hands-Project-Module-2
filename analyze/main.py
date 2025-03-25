"""Main module for queue implementation analysis."""

from typing import Type, Any, Dict, List
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

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


def run_tests(queue_class: Type[Any], size: int) -> TimingResult:
    """Run performance tests on a queue implementation.

    Args:
        queue_class: The queue class to test
        size: The size of the data structure to test with

    Returns:
        TimingResult containing the performance metrics
    """
    queue = queue_class()
    result = queue.timing_result

    # Test enqueue
    for i in range(size):
        queue.enqueue(i)

    # Test dequeue
    for _ in range(size // 2):
        queue.dequeue()

    # Test peek
    for _ in range(size // 3):
        queue.peek()

    # Test length and empty checks
    for _ in range(size // 4):
        len(queue)
        queue.is_empty()

    # Test concatenation
    queue2 = queue_class()
    queue2.enqueue(1)
    queue + queue2
    queue += queue2

    return result


def create_table(result: TimingResult, size: int) -> Table:
    """Create a table showing timing information."""
    # Determine implementation type from result name
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
    table.add_column("Ops/second", justify="right", style="blue")

    # Show all operations with non-zero time
    for op_name, (time, elements) in sorted(result.operations.items()):
        if time > 0 and elements > 0:
            time_ms = time * 1000  # Convert to milliseconds
            time_per_element_ms = (time / elements) * 1000  # Convert to milliseconds
            ops_per_second = elements / time
            table.add_row(
                op_name,
                f"{time_ms:.6f}",
                f"{elements:,}",
                f"{time_per_element_ms:.6f}",
                f"{ops_per_second:,.2f}",
            )

    return table


def get_selected_approaches(dll: bool, sll: bool, array: bool) -> List[QueueApproach]:
    """Get list of selected queue approaches based on command line options."""
    if not any([dll, sll, array]):
        return list(QueueApproach)

    approaches = []
    if dll:
        approaches.append(QueueApproach.dll)
    if sll:
        approaches.append(QueueApproach.sll)
    if array:
        approaches.append(QueueApproach.array)
    return approaches


@app.command()
def main(
    size: int = typer.Option(1000, "--size", "-s", help="Size of the data structure"),
    dll: bool = typer.Option(False, "--dll", help="Test DLL Queue implementation"),
    sll: bool = typer.Option(False, "--sll", help="Test SLL Queue implementation"),
    array: bool = typer.Option(
        False, "--array", help="Test Array Queue implementation"
    ),
):
    """Run performance analysis on queue implementations.

    Example usage:
      analyze --size 1000           # Test all implementations with size 1000
      analyze --size 2000 --dll     # Test only DLL implementation with size 2000
      analyze --size 500 --sll      # Test only SLL implementation with size 500
    """
    # Print welcome message
    console.print(
        Panel(
            "[bold]Queue Implementation Performance Analysis[/bold]",
            title="Queue Analysis Tool",
            border_style="blue",
        )
    )

    # Get selected approaches
    approaches = get_selected_approaches(dll, sll, array)

    # Test each implementation
    for approach in approaches:
        queue_class = QUEUE_IMPLEMENTATIONS[approach]
        result = run_tests(queue_class, size)
        console.print(Panel(create_table(result, size)))


if __name__ == "__main__":
    app()

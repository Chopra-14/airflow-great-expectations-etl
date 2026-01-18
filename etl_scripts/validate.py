from great_expectations.data_context import DataContext
from great_expectations.checkpoint import CheckpointResult


def run_checkpoint(checkpoint_name: str) -> None:
    """
    Run a Great Expectations checkpoint.

    Args:
        checkpoint_name (str): Name of the checkpoint to run

    Raises:
        RuntimeError: If data validation fails
    """

    context = DataContext()

    # Run checkpoint
    result: CheckpointResult = context.run_checkpoint(
        checkpoint_name=checkpoint_name
    )

    # If validation fails, stop pipeline
    if not result["success"]:
        raise RuntimeError(
            f"Great Expectations validation failed for checkpoint: {checkpoint_name}"
        )


if __name__ == "__main__":
    # Example usage (manual testing)
    run_checkpoint("raw_data_checkpoint")
    run_checkpoint("transformed_data_checkpoint")

    print("Great Expectations validation passed successfully.")

from rich import print
from typing import Optional


class Printer:
    def __init__(self):
        self.color_map = {
            "info": "blue",
            "success": "green",
            "warning": "yellow",
            "error": "red",
        }
        # Define labels
        self.labels = {
            "info": "INFO",
            "success": "SUCCESS",
            "warning": "WARNING",
            "error": "ERROR",
        }
        # Calculate the length of the longest label
        self.max_label_length = max(len(label) for label in self.labels.values())

    def _get_centered_label(self, label_type: str) -> str:
        """Return a centered label"""
        label = self.labels[label_type]
        padding = self.max_label_length - len(label)
        left_padding = padding // 2
        right_padding = padding - left_padding
        return " " * left_padding + label + " " * right_padding

    def print(
        self, message_type: str, message: str, color: Optional[str] = None
    ) -> None:
        """Generic message printing method"""
        if message_type not in self.labels:
            raise ValueError(f"Unknown message type: {message_type}")

        color = color or self.color_map.get(message_type, "white")
        label = self._get_centered_label(message_type)
        print(
            f"[{color}][bold #ffffff on {color}]{label}[/bold #ffffff on {color}] {message}[/{color}]"
        )

    def info(self, message: str) -> None:
        self.print("info", message)

    def success(self, message: str) -> None:
        self.print("success", message)

    def warning(self, message: str) -> None:
        self.print("warning", message)

    def error(self, message: str) -> None:
        self.print("error", message)

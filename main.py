from textual.app import App, ComposeResult
from textual.widgets import Button, Digits, Footer, Header, Label
from textual.containers import HorizontalGroup, VerticalGroup, VerticalScroll

class DayFrame(VerticalGroup):
    """A singular day in the calendar"""
    def compose(self) -> ComposeResult:
        yield Label("Day")
        yield Label("Event")
        yield Button("Delete")
class TodoApp(App):
    """A textual organistion app."""

    CSS_PATH = "./to-do.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield VerticalScroll(DayFrame(), DayFrame(), DayFrame())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = TodoApp()
    app.run()
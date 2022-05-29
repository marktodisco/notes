import markdown
import pytest
from src.readers import MarkdownNote


@pytest.fixture
def note_2022_05_26() -> MarkdownNote:
    return MarkdownNote("./tests/data/2022-05-26.md")


@pytest.fixture
def note_2022_05_27() -> MarkdownNote:
    return MarkdownNote("./tests/data/2022-05-27.md")


def test_markdown_note(note_2022_05_26: MarkdownNote, note_2022_05_27: MarkdownNote):
    notes = [note_2022_05_26, note_2022_05_27]
    assert len(notes) == 2
    assert notes[0].text == "# Header 1"
    assert notes[1].text == "\n".join(
        [
            "# Header 1",
            "",
            "## Header 2",
            "",
            "### Header 3",
            "",
            "#### Header 4",
            "",
            "##### Header 5",
            "",
            "###### Header 6",
            "",
            "This is the body.",
            "",
            "- item 1",
            "- item 2",
            "",
            "*italic*",
            "**bold**",
            "***bold and italic***",
        ]
    )


def test_markdown_to_html(note_2022_05_26: MarkdownNote, note_2022_05_27: MarkdownNote):
    assert note_2022_05_26.to_html() == "<h1>Header 1</h1>"
    assert note_2022_05_27.to_html() == "\n".join(
        [
            "<h1>Header 1</h1>",
            "<h2>Header 2</h2>",
            "<h3>Header 3</h3>",
            "<h4>Header 4</h4>",
            "<h5>Header 5</h5>",
            "<h6>Header 6</h6>",
            "<p>This is the body.</p>",
            "<ul>",
            "<li>item 1</li>",
            "<li>item 2</li>",
            "</ul>",
            "<p><em>italic</em>",
            "<strong>bold</strong>",
            "<strong><em>bold and italic</em></strong></p>",
        ]
    )

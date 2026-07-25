# Meeting Action Extractor

A Python CLI tool that converts unstructured meeting notes into a structured business report using the OpenAI API.

The tool extracts:

- Summary
- Key decisions
- Action items
- Owners
- Priority
- Open questions

This project was built to practice working with APIs, environment variables, prompt design, and command-line Python applications.

## Tech Stack

- Python
- OpenAI API
- python-dotenv

## Project Structure

```text
meeting-action-extractor/
├── main.py
├── requirements.txt
├── README.md
└── .env
```

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd meeting-action-extractor
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file:

```bash
touch .env
```

5. Add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## How To Run

Run the app:

```bash
python main.py
```

Paste your meeting notes into the terminal. When finished, type `END` on a new line and press Enter.

Example input:

```text
Team discussed launching the new landing page next Friday.
Priya will finalize the copy by Wednesday.
Rahul will review analytics tracking before launch.
The team decided to keep the first release simple and add personalization later.
END
```

Example output:

```text
SUMMARY
The team discussed plans for launching the new landing page next Friday.

KEY DECISIONS
- The first release will be kept simple.
- Personalization will be added later.

ACTION ITEMS
- Priya will finalize the copy by Wednesday.
- Rahul will review analytics tracking before launch.

OWNERS
- Priya
- Rahul

PRIORITY
Landing page launch preparation.

OPEN QUESTIONS
- No explicit open questions identified.
```

## What I Learned

Through this project, I practiced:

- Calling an external API from Python
- Managing API keys with environment variables
- Designing prompts for structured output
- Building a simple command-line workflow
- Handling user input and basic errors

## Future Improvements

- Add support for reading notes from a `.txt` file
- Add Markdown or JSON output options
- Save generated reports to a file
- Add automated tests for prompt creation and input validation
- Improve error handling for API failures

## CV Description

Built a Python CLI tool using the OpenAI API to convert unstructured meeting notes into structured business reports, extracting summaries, decisions, action items, owners, priorities, and open questions with environment-based API key management.

import os
from dotenv import load_dotenv
from openai import OpenAI


def get_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY was not found in the .env file. Please check .env")

    return api_key


def collect_meeting_notes():
    print("Paste your meeting notes below as input")
    print("When you are finished, type END on a new line and press Enter. \n")

    lines = []

    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    notes = "\n".join(lines).strip()

    if not notes:
        raise ValueError("No meeting notes were entered.")

    return notes


def build_prompt(notes):
    return f"""
You are a business meeting assistant.

Your task is to convert raw meeting notes into a structured report.

Rules:
- Only use information that is explicitly present in the notes.
- Do not invent names, deadlines, decisions, or actions.
- If something is not clear, place it under Open Questions.
- If no explicit decisions are present, say: No explicit decisions identified.
- If no explicit action items are present, say: No explicit action items identified.
- Keep the summary concise.

Return the output in exactly this format:

SUMMARY
...

KEY DECISIONS
- ...

ACTION ITEMS
- ...

OWNERS
- ...

PRIORITY
...

OPEN QUESTIONS
- ...

Meeting notes:
{notes}
""".strip()


def analyze_notes(client, prompt):
    response = client.responses.create(
        model = "gpt-4.1-mini",
        input = prompt,
    )

    return response.output_text.strip()


def main():
    try:
        api_key = get_api_key()
        client = OpenAI(api_key=api_key)

        notes = collect_meeting_notes()
        prompt = build_prompt(notes)
        result = analyze_notes(client, prompt)

        print("\n" + "=" * 50)
        print("STRUCTURED MEETING REPORT")
        print("=" * 50)
        print(result)

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
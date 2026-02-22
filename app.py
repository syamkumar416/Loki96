import textwrap

def summarize(text):
    sentences = text.split(". ")
    if len(sentences) <= 2:
        return text
    return sentences[0] + ". " + sentences[-1]

def rewrite(text):
    return text.capitalize()

def word_count(text):
    words = text.split()
    return len(words)

def main():
    print("📜 Welcome to Scriptoria - Smart Writing Assistant\n")

    text = input("Enter your text:\n")

    print("\nChoose Operation:")
    print("1. Word Count")
    print("2. Summarize")
    print("3. Rewrite (Basic Clean)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        print("\n🧮 Word Count:", word_count(text))

    elif choice == "2":
        print("\n📝 Summary:")
        print(textwrap.fill(summarize(text), width=70))

    elif choice == "3":
        print("\n✏ Rewritten Text:")
        print(textwrap.fill(rewrite(text), width=70))

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

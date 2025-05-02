# Natural Language Processing (NLP) Basics

**Basics of NLP**

## 1. Segmentation

**Definition:** Dividing raw text into smaller, meaningful units—typically sentences or paragraphs.

**Why it matters:** Downstream tasks (like translation or summarization) require knowing the boundaries of thoughts and ideas.

**Key points:**

* **Sentence segmentation:** Identify sentence boundaries (e.g., periods, question marks).
* **Paragraph segmentation:** Split text on double line breaks or indentation.

**Example:**
Original text:

> Hello there! How are you doing today? I hope you’re well.

**After segmentation:**

1. **Sentence 1:** "Hello there!"
2. **Sentence 2:** "How are you doing today?"
3. **Sentence 3:** "I hope you’re well."

Each sentence can now be processed independently.

---

## 2. Tokenizing

**Definition:** Breaking a sentence into individual pieces called *tokens* (words, punctuation, numbers).

**Why it matters:** Tokens are the atomic units NLP models analyze (word counts, embeddings, etc.).

**Types of tokenization:**

* **Word-based:** Splits on whitespace and punctuation (e.g., "it's" → \["it", "'s"]).
* **Subword (e.g., Byte-Pair Encoding):** Further splits rare words into common sub-parts (e.g., "unhappiness" → \["un", "happi", "ness"]).

**Example:**

> Sentence: "GPT-3, released in 2020, revolutionized NLP!"

* **Word tokens:** \["GPT-3", ",", "released", "in", "2020", ",", "revolutionized", "NLP", "!"]
* **Subword tokens (hypothetical):** \["G", "PT", "-", "3", ",", "re", "leased", …]

---

## 3. Stop Words

**Definition:** Common words (e.g., "the", "is", "and") that carry little semantic weight.

**Why it matters:** Removing them reduces vocabulary size and focuses on meaningful tokens.

**Typical stop-word list:**

> \["a", "an", "the", "in", "on", "and", "is", "to", "it"]

**Example:**

* **Original tokens:** \["It", "is", "a", "sunny", "day"]
* **After removal:** \["sunny", "day"]

Notice how we retain the content words that describe the scene.

---

## 4. Stemming

**Definition:** Heuristic process to trim words to their *stems* by chopping off endings.

**Why it matters:** Groups word variants under a common root, simplifying analysis.

**Common algorithm:** Porter Stemmer (removes suffixes like -ing, -ed).

**Example:**

* Input words: \["connect", "connected", "connecting", "connection"]
* Porter-stemmed: \["connect", "connect", "connect", "connect"]

⚠️ **Caveat:** Stemming may produce non-dictionary forms (e.g., "comput" from "computer").

---

## 5. Lemmatization

**Definition:** Converts words to their dictionary *lemmata* (base forms) using vocabulary and rules.

**Why it matters:** Produces real words, respects context (POS tags).

**Example:**

* Input: \["better", "running", "geese"]
* Lemmatized (with POS): \["good", "run", "goose"]

➤ Unlike stemming, lemmatization knows that "better" → "good", not "bett".

---

## 6. Part-of-Speech (POS) Tagging

**Definition:** Labeling each token with its grammatical role (noun, verb, adjective, etc.).

**Why it matters:** Reveals sentence structure and guides tasks like parsing and named-entity recognition.

**Common tags (Penn Treebank set):**

| Tag | Meaning                   | Example |
| --- | ------------------------- | ------- |
| NN  | Noun                      | dog     |
| VBZ | Verb, 3rd-person singular | runs    |
| JJ  | Adjective                 | blue    |
| RB  | Adverb                    | quickly |

**Example:**

> Sentence: "The quick brown fox jumps."

* The/DT  quick/JJ  brown/JJ  fox/NN  jumps/VBZ  ./.

Here, `/DT`, `/JJ`, `/NN`, `/VBZ` are POS tags.

---

## 7. Named Entity Recognition (NER)

**Definition:** Identifying and classifying *entities* in text into categories like Person, Organization, Location, Date.

**Why it matters:** Extracts structured facts (who did what, where, when).

**Common entity types:**

* **PERSON:** People’s names
* **ORG:** Organizations (companies, institutions)
* **LOC:** Locations (cities, countries)
* **DATE:** Dates and times

**Example:**

> "Apple Inc. was founded by Steve Jobs in Cupertino in 1976."

* \[Apple Inc.]/ORG  \[Steve Jobs]/PERSON  \[Cupertino]/LOC  \[1976]/DATE

---

## 8. Text Normalization

**Definition:** Standardizing text to a uniform format before analysis.

**Key steps:**

1. **Lowercasing:** "NLP" → "nlp"
2. **Unicode normalization:** "café" → "cafe"
3. **Contraction expansion:** "don't" → "do not"
4. **Accents removal:** "naïve" → "naive"

**Example:**

* Original: "I Can't wait to analyse this café’s menu!"
* Normalized: "i can not wait to analyze this cafes menu"

---

## 9. Regular Expressions (Regex)

**Definition:** Patterns to search, match, or manipulate text based on character sequences.

**Why it matters:** Quickly extract emails, phone numbers, dates, etc.

**Common regex symbols:**

* `.` : any character
* `*` : zero or more repeats
* `+` : one or more repeats
* `\d` : digit
* `\w` : word character (letter, digit, underscore)

**Example patterns:**

| Task              | Pattern                 | Matches                                     |
| ----------------- | ----------------------- | ------------------------------------------- |
| Email address     | `\S+@\S+\.\S+`          | [user@example.com](mailto:user@example.com) |
| Date (YYYY-MM-DD) | `\d{4}-\d{2}-\d{2}`     | 2025-05-03                                  |
| Phone (US)        | `\(\d{3}\) \d{3}-\d{4}` | (123) 456-7890                              |

---

## 10. Chunking & Chinking

**Chunking:** Grouping tokens into higher-level phrases using POS patterns (e.g., noun phrases).

**Chinking:** Removing unwanted tokens from within those chunks.

**Why it matters:** Extracts multi-word expressions (e.g., "financial crisis") and refines them.

**Process example:**

1. **Sentence:** "The seasoned software engineer fixed the bug quickly."
2. **POS tags:** The/DT seasoned/JJ software/NN engineer/NN fixed/VBD the/DT bug/NN quickly/RB
3. **Chunk grammar:** `NP: {<DT>?<JJ>*<NN>+}` → finds Noun Phrases

   * Chunks found: \["The seasoned software engineer"], \["the bug"]
4. **Chinking grammar:** `}<JJ>{` → removes adjectives inside chunks

   * After chinking: \["The engineer"], \["the bug"]

---

## 11. WordNet

**Definition:** A large lexical database that groups English words into *synsets* (sets of synonyms) and records semantic relations.

**Key relations:**

* **Synonymy:** Words with similar meaning in the same synset.
* **Antonymy:** Opposite meanings.
* **Hypernymy:** "Is-a" hierarchy (e.g., dog → animal).
* **Hyponymy:** Specific instances (animal → dog, cat).

**Example concept:**

* **Word:** "bird"

  * **Synsets:** {"bird", "aves"}
  * **Hypernym:** "vertebrate"
  * **Hyponyms:** "sparrow", "eagle", "penguin"
  * **Antonyms:** (often none for nouns)

Use WordNet to find synonyms, examine word hierarchies, and compute word similarity.

---

Feel free to use this guide as a reference for lectures or self-study. Each section provides a solid foundation—you can build on these concepts with hands-on exercises and real data examples. Happy teaching! 🎉

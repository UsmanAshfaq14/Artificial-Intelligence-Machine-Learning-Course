# Probability and Statistical Distributions

This repository provides an in-depth exploration of probability theory and its related concepts. The document covers fundamental definitions, formulas, and working principles for various topics such as Probability, Joint, Marginal and Conditional Probability, Probability Distributions (both discrete and continuous), as well as specific distributions like Normal, Binomial, and Poisson. Additionally, it delves into Bayesian Probability, explaining its rationale and applications. The explanations herein are designed to be self-explanatory and descriptive, providing essential information for both beginners and advanced users.

## Table of Contents
- [Probability](#probability)
- [Joint, Marginal, and Conditional Probability](#joint-marginal-and-conditional-probability)
- [Probability Distributions](#probability-distributions)
  - [Discrete Probability](#discrete-probability)
  - [Continuous Probability](#continuous-probability)
- [Specific Probability Distributions](#specific-probability-distributions)
  - [Normal Distribution](#normal-distribution)
  - [Binomial Distribution](#binomial-distribution)
  - [Poisson Distribution](#poisson-distribution)
- [Bayesian Probability](#bayesian-probability)
- [Methodology and Working](#methodology-and-working)
- [References](#references)

## Probability
Probability is a measure that quantifies the likelihood of an event occurring within a defined sample space. The probability of an event $$A$$ is defined as:

$$ P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}} $$

Key points include:
- **Sample Space:** The set of all possible outcomes.
- **Event:** A subset of the sample space.
- **Axioms of Probability:** Including non-negativity, normalization ($$ P(S) = 1 $$), and additivity for mutually exclusive events.

## Joint, Marginal, and Conditional Probability
Understanding the relationship between events is crucial in probability theory.

### Joint Probability
- **Definition:** The probability of two events $$A$$ and $$B$$ occurring simultaneously is denoted as $$ P(A \cap B) $$.
- **Formula:** For independent events, it simplifies to:
  
$$ P(A \cap B) = P(A) \times P(B) $$

### Marginal Probability
- **Definition:** The probability of an event irrespective of the outcomes of other variables. It is obtained by summing or integrating over the possible values of the other variables.
- **Example:** If $$A$$ and $$B$$ are joint events, then the marginal probability of $$A$$ is:

$$ P(A) = \sum_{B} P(A, B) $$

### Conditional Probability
- **Definition:** The probability of an event $$A$$ given that another event $$B$$ has occurred is denoted as $$ P(A|B) $$.
- **Formula:**

$$ P(A|B) = \frac{P(A \cap B)}{P(B)} \quad \text{(provided } P(B) > 0\text{)} $$

- **Bayes’ Theorem:** An essential tool for updating probabilities:

$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$

## Probability Distributions
Probability distributions describe how probabilities are assigned to different outcomes. They are broadly categorized into:

### Discrete Probability
- **Definition:** Deals with countable outcomes.
- **Examples:** Binomial, Poisson, and Geometric distributions.

### Continuous Probability
- **Definition:** Deals with outcomes over a continuous range.
- **Examples:** Normal, Exponential, and Uniform distributions.

## Specific Probability Distributions

### Normal Distribution
- **Definition:** Also known as the Gaussian distribution, it is a continuous probability distribution characterized by its bell-shaped curve.
- **Key Parameters:** Mean ($$ \mu $$) and Standard Deviation ($$ \sigma $$).
- **Formula:**

$$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} \, e^{ -\frac{(x-\mu)^2}{2\sigma^2} } $$

- **Properties:** Symmetric about the mean, where approximately 68% of the data falls within one standard deviation, 95% within two, and 99.7% within three.

### Binomial Distribution
- **Definition:** A discrete distribution representing the number of successes in a fixed number of independent Bernoulli trials.
- **Key Parameters:** Number of trials ($$ n $$) and probability of success in a single trial ($$ p $$).
- **Formula:**

$$ P(X = k) = \binom{n}{k} \, p^k \, (1-p)^{n-k} $$

- **Applications:** Used in scenarios with two possible outcomes (e.g., success/failure, yes/no).

### Poisson Distribution
- **Definition:** A discrete distribution expressing the probability of a given number of events occurring in a fixed interval of time or space.
- **Key Parameter:** The average number of occurrences ($$ \lambda $$).
- **Formula:**

$$ P(X = k) = \frac{\lambda^k \, e^{-\lambda}}{k!} $$

- **Applications:** Commonly used for modeling rare events.

## Bayesian Probability
Bayesian probability offers a framework for updating beliefs in light of new evidence. It is fundamentally based on Bayes' theorem:

$$ P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)} $$

Where:
- $$ P(H) $$ is the prior probability of the hypothesis.
- $$ P(E|H) $$ is the likelihood of observing the evidence given the hypothesis.
- $$ P(E) $$ is the total probability of the evidence.
- $$ P(H|E) $$ is the posterior probability after taking the evidence into account.

### Key Concepts:
- **Prior:** Initial belief before seeing the data.
- **Posterior:** Updated belief after incorporating the evidence.
- **Likelihood:** Probability of observing the data under different hypotheses.
- **Bayesian Inference:** A method of statistical inference in which Bayes' theorem is used to update the probability for a hypothesis as more evidence or information becomes available.

## Methodology and Working
This document synthesizes comprehensive theoretical explanations with descriptive narratives to make the complex concepts of probability accessible and understandable. The approach includes:
- **Theoretical Foundations:** Detailed definitions and mathematical formulations.
- **Step-by-Step Explanations:** Elucidation of how to derive and interpret key formulas.
- **Comparative Analysis:** Highlighting differences between discrete and continuous distributions.
- **Applications:** Practical examples and scenarios where each concept is applicable.
- **Visualization Techniques:** Although the Python code is not included here, practical implementations using code (e.g., plotting distributions) were developed to illustrate these concepts in action.

## References
- **Geeks for Geeks:** The content and explanations presented in this document are inspired by detailed descriptions and examples available on Geeks for Geeks.
- Additional textbooks and academic sources on probability theory and statistical distributions have also influenced the comprehensive nature of this guide.

---

*This README serves as a comprehensive guide for understanding the foundational and advanced aspects of probability and probability distributions. For further insights and hands-on examples, please refer to the associated documentation and code examples in this repository.*

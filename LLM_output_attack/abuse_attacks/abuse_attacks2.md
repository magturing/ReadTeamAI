LLM Abuse Attacks

As discussed in the previous section, adversaries may weaponize LLMs to generate harmful, biased, or unethical content such as hate speech, disinformation, or deepfakes for various malicious objectives. This weaponization of LLMs can include spreading hate speech to incite violence, spreading disinformation to mislead and influence public opinion or even democratic elections, spreading deepfakes to damage people's reputations, enabling fraud, or undermining trust in digital media. These abuse attacks are particularly effective at achieving their goal, as LLM-generated fake news is often more challenging to detect than human-written fake news.

We will not discuss the technical details of LLM abuse campaigns for ethical reasons. However, we will briefly touch on a high-level overview of misinformation generation and hate speech detection.
LLM Misinformation Generation

Modern LLMs are typically trained to display resilience against misinformation related to sensitive real-world information. For instance, LLMs will happily write a fake story about something obviously fake or unrelated to sensitive topics that may cause harm in the real world. As such, an LLM might write a fake news article about aliens working at HackTheBox boosting students' IQ:
Fake news article titled 'Leaked Documents Reveal Aliens Working at HackTheBox Academy'. Claims extraterrestrial beings are employed to develop hacking challenges, boosting student IQ by 50 points.

On the other hand, the same LLM will not comply with writing an article about vaccines causing autism:
Request to write a fake news article about vaccines causing autism. Response: Refusal to create misinformation on serious topics, but offers to help with satire or parody.

This resilience is robust against direct prompts for misinformation. However, several strategies exist to bypass it, including jailbreaking, as discussed in the Prompt Injection Attacks module. Additionally, we can task the LLM with writing an article about a fake event and later edit the generated response to fit our misinformation needs. For instance, we could ask for an article about a fictitious item XYZ causing autism and replace all occurrences of XYZ in the article with the term vaccines:
Satirical-style fake news article titled 'SHOCKING STUDY: Common Household Item XYZ Linked to Autism!' Claims a study suggests XYZ may alter brain development.
Evading Hate Speech Detection

As a second case study, let us explore evading LLM-based hate speech detectors based on this paper. Before diving in, let us first establish a definition of hate speech. According to the United Nations, hate speech is any kind of communication in speech, writing or behavior, that attacks or uses pejorative or discriminatory language with reference to a person or a group on the basis of who they are, in other words, based on their religion, ethnicity, nationality, race, colour, descent, gender or other identity factor.

As LLMs significantly lower the cost of misinformation and hate campaigns, they are quickly becoming more prevalent. In large-scale hate speech campaigns, the adversaries' goal is typically to generate and spread hate speech without detection by hate speech detection measures, including algorithmic and human-based detection measures.

There are many popular AI-based hate speech detectors, such as HateXplain or Detoxify. These models typically process a text input and assign a toxicity score. If the input scores higher than a predefined threshold, we can classify it as hate speech. These detectors work reasonably well on LLM-generated hate speech samples. When evaluating different hate speech detectors, it is essential to remember that different detectors may operate based on a different definition of hate speech, resulting in different results.

To evade hate speech detectors, adversaries may apply different adversarial attacks to the LLM-generated hate speech samples. These include:

    Character-level modifications: These adversarial attacks modify text input by scoring individual tokens and modifying the most important tokens. An example of this type of adversarial attack is DeepWordBug. Character-level modifications can include the following operations:
        Swap: Swapping two adjacent characters, e.g., HackTheBox becomes HackhTeBox
        Substitution: Substituting a character with a different character, e.g., HackTheBox becomes HackTueBox
        Deletion: Deleting a character, e.g., HackTheBox becomes HackTeBox
        Insertion: Insertion a character, e.g., HackTheBox becomes HackTheBoux
    Word-level modifications: These adversarial attacks modify text input by replacing words with synonyms. An example would be PWWS, which greedily replaces words with synonyms until the classification changes.
    Sentence-level modifications: This adversarial attack modifies text input by paraphrasing it. An LLM can perform this modification by tasking it with paraphrasing the provided input.

The adversarial attacks on hate speech detectors are effective in evading detection, proving that human validation of hate speech is required to detect hate speech effectively. These evasion techniques can apply to other types of abuse attacks as well, including dangerous content, sexually explicit content, or any other type of content that violates a company's policy.


Readings :- "https://arxiv.org/abs/2501.16750"

Hate speech detectors :- https://github.com/JHL-HUST/PWWS
https://github.com/QData/deepWordBug
https://github.com/unitaryai/detoxify
https://github.com/hate-alert/HateXplain

article :- "https://www.un.org/en/hate-speech/understanding-hate-speech/what-is-hate-speech"

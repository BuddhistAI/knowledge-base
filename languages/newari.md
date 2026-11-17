---
id: newari
title: Newari (Nepal Bhasa)
short_title: Newari
kind: classical and modern
group: Indic
countries: [Nepal]
scripts: [Devanagari, Ranjana, Newar (Nepal Lipi)]
speakers: about 880,000 native speakers (2021 census; Wikipedia [1])
speakers_n: 880000
speakers_year: 2021
speakers_source: https://en.wikipedia.org/wiki/Newar_language
speakers_basis: first-language speakers
directory_names: [Newari]
resource_level: low
google_translate: yes (since 2024)
recommendation: Google Translate plus a frontier LLM with native review
confidence: low
updated: 2026-11
contributors: []
---

# Newari (Nepal Bhasa)

Newari (Nepal Bhasa) is the language of the Newar people of the Kathmandu Valley, the home of Newar Buddhism. The language is endangered [1]. Google Translate added it in 2024, but there is no public test of translation into Newari.

## Summary

| | |
| --- | --- |
| Where | Nepal (Kathmandu Valley) |
| Speakers | about 880,000 native speakers (2021 census); UNESCO "Definitely endangered" [1] |
| Script | Ranjana, Devanagari, Newar script (Nepal Lipi), Bhujimol [1] |
| AI resources | low |
| Google Translate | yes, added in June 2024 [2] [3]; NMT only in the Cloud API [4] |
| Microsoft Translator | no [5] |
| Speech to text | not in Whisper [6]; Meta Omnilingual ASR covers it [7]; Nwāchā Munā corpus (2026) [8] |
| Best evidence on translation quality | none found |

## Writing and text input

Newari is written in several scripts: Ranjana, Devanagari, the Newar script (Nepal Lipi) and Bhujimol [1]. Most digital Newari text and AI work uses Devanagari. For example, the Nwāchā Munā speech corpus uses Devanagari transcripts [8]. A Unicode block for the Newa script exists; we did not verify its details in this research.

OCR: we found no verified public OCR model or ground-truth data for Ranjana or the Newar script. Two items on Ranjana recognition (from Khwopa College and Kathmandu University) appeared in search results, but we did not open them.

## Data

- We found no Newari–English parallel corpus of useful size.
- Manuscripts: the Nepalese-German Manuscript Cataloguing Project (NGMCP) catalogue includes many Buddhist Sanskrit and Newar manuscripts. We saw it only in search results and did not verify the details.
- Web corpus sizes for Newari: not verified.

## Speech

- **Nwāchā Munā (Kathmandu University ILPRL, 2026)** is the first public Newari speech benchmark we found: 5.39 hours of transcribed speech, 5,727 utterances, 18 native speakers, Devanagari transcripts [8].
  - Best character error rate (CER): 17.59% (NepConformer with data augmentation). Best word error rate (WER): 48.46% (NepConformer with a 5-gram language model). Lower is better.
  - Fine-tuned Whisper-Small: 18.76% CER, 51.44% WER.
  - A Nepali model used zero-shot: 52.54% CER, 98.68% WER. So a Nepali model does not work for Newari without training.
  - The paper is CC BY-NC-SA 4.0. The data license is not stated separately.
- OpenAI Whisper does not list Newari [6].
- Meta Omnilingual ASR (November 2025) reports a CER of 2.2 for new_Deva, with 37.9 hours of training audio [7]. This test set is small and narrow, so do not compare it with the Nwāchā Munā numbers.

## Machine translation

**Support.** Google Translate added "Nepalbhasa (Newari)" in its June 2024 expansion [2]. Local news covered this on 2024-06-28 [3]. In the Google Cloud API, Newari is NMT only, not in the Translation LLM [4]. Microsoft Translator does not support Newari [5]. Newari is not in the FLORES-200 test set, so there are no FLORES scores [9].

**Evidence.** None. We found no benchmark and no published human evaluation for translation into Newari with any system. Any quality claim would be anecdotal.

## AI projects

- Nwāchā Munā: Newari speech corpus and models by Kathmandu University ILPRL. Code: github.com/ilprl/nwacha-muna. Data and models are on Hugging Face (ilprl-docse collection) [8].

## Recommendation

To translate into Newari today, use Google Translate (the only system with official support) and test a current frontier model next to it. A native Newari reviewer must check all output, and should check that Buddhist terms follow Newar usage. Confidence is low: there is no test of any system.

Test first: ask native speakers to translate 50 to 100 short English sentences into Newari in Devanagari, half general and half Buddhist (for example, from a prayer or a festival text). Use them as a small test set with chrF++ and native review. This set would also be the first public test for translation into Newari. Newari is not yet measured on the BuddhistAI leaderboard.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Newari. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (1)

- [Nepalese-German Manuscript Cataloguing Project (NGMCP)](https://ngmcp.fdm.uni-hamburg.de/mediawiki/index.php/NGMCP) (University of Hamburg with the National Archives of Nepal): Catalogue of the Nepalese manuscripts that the Nepal-German Manuscript Preservation Project microfilmed (more than 114,500 items in Sanskrit, Newari, Nepali and other languages).

**Datasets** (1)

- [Nwāchā Munā (Newari speech)](https://huggingface.co/collections/ilprl-docse/nwacha-muna) (Kathmandu University (ILPRL)): 5.39 hours of transcribed Newari (Nepal Bhasa) speech in Devanagari, with speech recognition baseline models.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Newar language](https://en.wikipedia.org/wiki/Newar_language), read 2026-11-17
2. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
3. [ekantipur / Kathmandu Post: Newari language included in Google Translate, 2024-06-28](https://ekantipur.com/en/business/2024/06/28/newari-language-included-in-google-translate-37-06.html), read 2026-11-17
4. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
5. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
6. [OpenAI Whisper tokenizer.py (language list)](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py), read 2026-11-17
7. [Meta Omnilingual ASR, per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
8. [Nwāchā Munā, arXiv 2603.07554v2, revised 2026-03-30](https://arxiv.org/html/2603.07554), read 2026-11-17
9. [Robinson et al. 2023, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17

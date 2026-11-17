---
id: himalayan-tibetic
title: Ladakhi and other Himalayan languages
short_title: Ladakhi and others
kind: modern
group: Tibetic
countries: [India, Nepal, Pakistan]
scripts: [Tibetan]
speakers: about 400,000 together: Ladakhi 110,826 (2011 census), Sherpa about 260,000, Sikkimese about 25,000 (via Wikipedia)
speakers_n: 395826
speakers_year: 2011 to 2021
speakers_source: https://en.wikipedia.org/wiki/Ladakhi_language
speakers_basis: Ladakhi, Sherpa and Sikkimese added together
directory_names: [Ladakhi, Sikkimese, Sherpa]
resource_level: very low
google_translate: no
recommendation: Human translation; AI only for drafts
confidence: low
updated: 2026-11
contributors: []
---

# Ladakhi and other Himalayan languages

This page covers smaller Tibetic languages of the Himalaya, such as Ladakhi (Ladakh, India), Sikkimese (Sikkim, India), Sherpa (Nepal) and Balti (Baltistan, Pakistan). Many Buddhist communities speak these languages and use Classical Tibetan for texts and ritual. We found no machine translation system and no test for any of them, so a human translator must lead.

## Summary

| | |
| --- | --- |
| Where | Himalayan regions of India, Nepal and Pakistan |
| Speakers | about 400,000 together: Ladakhi 110,826 (2011 census), Sherpa about 260,000, Sikkimese about 25,000 (via Wikipedia) [6] |
| Script | Tibetan script (Balti: not verified) |
| AI resources | very low |
| Google Translate | no; Ladakhi and Sherpa are not in the June 2024 list [1] |
| Microsoft Translator | no [2] |
| Speech to text | not in Whisper [3]; other systems not verified |
| Best evidence on translation quality | none found |

## Writing and text input

Ladakhi, Sikkimese and Sherpa can be written in the Tibetan script, which is in Unicode. We did not verify how each community writes its language today. Balti is often said to be written mostly in Perso-Arabic script today, but we could not verify this.

Tibetan OCR models (BDRC, OpenPecha, Monlam AI; see the Tibetan page) may help with printed text in Tibetan script. This is not tested for these languages.

## Data

- We found no corpus for Ladakhi, Sikkimese, Sherpa or Balti.
- FineWeb-2 lists Tibetan and Dzongkha [4]. The table we read was cut off, so we could not see whether other Tibetic language codes are in it.
- Two general papers on low-resource Indian languages came up in our search, but we did not confirm that they include Ladakhi.

## Speech

- OpenAI Whisper does not list Ladakhi, Sikkimese, Sherpa or Balti [3].
- Meta Omnilingual ASR covers more than 1,600 languages [5]. We did not check whether Ladakhi, Sherpa or the other languages on this page are among them.
- We found no audio archive or speech dataset for these languages in this research.

## Machine translation

**Support.** Google Translate does not support Ladakhi or Sherpa; they are not in the June 2024 list of new languages [1]. Sikkimese is not supported either, as far as we found. Microsoft Translator does not list any of these languages [2]. We found no FLORES-200 test set or other public benchmark for them.

**Evidence.** None. There is no benchmark and no published report on AI translation into these languages.

**Possible workaround (not tested).** An AI model can write a draft in standard Tibetan, and a native speaker can then adapt it to the local language. This is an idea from our research notes, not a tested method. See the [Tibetan](tibetan.md) page for the quality of translation into Tibetan, which is itself low.

## AI projects

We found no AI project for these languages in this research. Projects listed in the Directory under these names appear below.

## Recommendation

To translate into Ladakhi, Sikkimese, Sherpa or Balti today, use a human translator. AI can help only with a draft, for example a draft in Tibetan or in a regional language that the translator then rewrites. Confidence is low, because there is no data and no test at all.

Test first: ask a native speaker to translate 20 to 50 short Buddhist sentences (for example, from a prayer or a short teaching). Use them as a small test set to compare a frontier model's direct output with the "Tibetan draft plus human adaptation" method. These languages are not yet measured on the BuddhistAI leaderboard. A small reviewed test set would be the first public resource for them.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Ladakhi, Sikkimese, Sherpa. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (0)

None listed yet.

**Datasets** (0)

None listed yet.

<!-- in-directory:end -->

## Sources

1. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
2. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
3. [OpenAI Whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
4. [FineWeb-2 README](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2/blob/cab26bb3cab1ca7c26bb13a48f80fc3d2def4620/README.md), read 2026-11-17
5. [Meta Omnilingual ASR README](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/README.md), read 2026-11-17
6. [Wikipedia, Ladakhi language, Sherpa language and Sikkimese language](https://en.wikipedia.org/wiki/Ladakhi_language), read 2026-11-17.

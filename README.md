# aoc_llm_eval
LLM evaluation using Advent Of Code puzzles

# Summary

| Model                      | Success Rate | Success Rate First Days | Success Rate Last Days |
|----------------------------|--------------|--------------------------|------------------------|
| **Llama 3.3 70B Instruct** | 55,0%        | 80,0%                     | 30,0%                  |
| **Mistral Large 2411**     | 55,0%        | 90,0%                     | 20,0%                  |
| **Qwen 2.5 72B Instruct**  | 30,0%        | 60,0%                     | 0,0%                   |
| **QwenCoder 32B Instruct** | 40,0%        | 70,0%                     | 10,0%                  |
| **Gemini 2.0 Flash Exp.**  | 60,0%        | 70,0%                     | 50,0%                  |
| **Claude 3.5 Sonnet**      | 70,0%        | 80,0%                     | 60,0%                  |
| **QwQ 32B Preview**        | 85,0%        | 100,0%                    | 70,0%                  |


# Detailed results

|               | Llama 3.3 70B Instruct | Mistral Large 2411 | Qwen 2.5 72B Instruct | QwenCoder 32B Instruct | Gemini 2.0 Flash Exp. | Claude 3.5 Sonnet | QwQ 32B Preview |
|---------------|------------------------|--------------------|-----------------------|------------------------|-----------------------|-------------------|------------------|
| **Day1 Part 1** | Passed                  | Passed              | Passed                 | Passed                  | Passed                 | Passed             | Passed            |
| **Day1 Part 2** | Passed                  | Passed              | Passed                 | Passed                  | Passed                 | Passed             | Passed            |
| **Day2 Part 1** | Passed                  | Passed              | Passed                 | Passed                  | Passed                 | Passed             | Passed            |
| **Day2 Part 2** | Passed                  | Passed              | Passed                 | Passed                  | Passed                 | Passed             | Passed            |
| **Day3 Part 1** | Passed                  | Passed              | Passed                 | Not Passed              | Not Passed             | Passed             | Passed            |
| **Day3 Part 2** | Passed                  | Passed              | Not Passed             | Not Passed              | Not Passed             | Passed             | Passed            |
| **Day4 Part 1** | Not Passed (1)          | Passed              | Passed                 | Passed                  | Passed                 | Passed             | Passed            |
| **Day4 Part 2** | Not Passed              | Not Passed          | Not Passed             | Not Passed              | Not Passed             | Not Passed         | Passed            |
| **Day5 Part 1** | Passed                  | Passed              | Not Passed             | Passed                  | Passed                 | Passed             | Passed            |
| **Day5 Part 2** | Passed                  | Passed              | Not Passed             | Passed                  | Passed                 | Not Passed         | Passed            |
| **Day6 Part 1** | Not Passed              | Not Passed          | Not Passed             | Not Passed              | Not Passed             | Passed             | Passed            |
| **Day6 Part 2** | Not Passed              | Not Passed          | Not Passed (2)         | Not Passed              | Not Passed             | Not Passed         | Passed            |
| **Day7 Part 1** | Passed                  | Not Passed          | Not Passed             | Not Passed              | Passed                 | Not Passed         | Passed            |
| **Day7 Part 2** | Passed                  | Not Passed          | Not Passed             | Not Passed              | Passed                 | Passed             | Passed            |
| **Day8 Part 1** | Not Passed              | Not Passed          | Not Passed (2)         | Not Passed              | Passed                 | Passed             | Passed            |
| **Day8 Part 2** | Not Passed              | Not Passed (2)      | Not Passed             | Not Passed              | Not Passed             | Not Passed         | Not Passed        |
| **Day9 Part 1** | Not Passed (3)          | Not Passed          | Not Passed (3)         | Not Passed              | Not Passed             | Passed             | Not Passed        |
| **Day9 Part 2** | Not Passed (3)          | Not Passed          | Not Passed (3)         | Not Passed (4)          | Passed                 | Not Passed         | Not Passed        |
| **Day10 Part 1**| Not Passed              | Passed              | Not Passed (5)         | Passed                  | Not Passed             | Passed             | Passed            |
| **Day10 Part 2**| Passed                  | Passed              | Not Passed (5)         | Not Passed              | Passed                 | Passed             | Passed            |

(1) The pattern was counted twice

(2) Invalid Syntax

(3) IndexError: string index out of range

(4) TypeError: 'bool' object is not iterable

(5) variable referenced before assignment

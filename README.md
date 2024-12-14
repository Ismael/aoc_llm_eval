# aoc_llm_eval
LLM evaluation using Advent Of Code puzzles

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
| **Success Ratio** | 61,1%                   | 61,1%                | 33,3%                   | 44,4%                   | 66,7%                  | 77,8%              | 94,4%             |
| **Success Ratio first 5 days** | 80,0%                | 90,0%                | 60,0%                   | 70,0%                   | 70,0%                  | 80,0%              | 100,0%            |
| **Success Ratio last 5 days** | 30,0%                | 20,0%                | 0,0%                    | 10,0%                   | 50,0%                  | 60,0%              | 70,0%             |

(1) The pattern was counted twice

(2) Invalid Syntax

(3) IndexError: string index out of range

(4) TypeError: 'bool' object is not iterable

(5) variable referenced before assignment
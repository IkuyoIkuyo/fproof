from anthropic import Anthropic
import json
import re
def main():

# /ai4math/users/qig/fproof/algebra_exercises_v4_11_0_cleaner_input.json
    model = "claude-3-5-sonnet-latest"
    client = Anthropic(
        base_url='https://api.openai-proxy.org/anthropic',
        api_key='sk-o6izkPNCPs7BfpH5qnYsUjgRDI4Dnvw5u11xh9O2s5sJENDB',
    )
    content = open("/ai4math/users/qig/fproof/prompt12informal.md", "r",encoding="utf-8").read()
    inp=json.load(open("/ai4math/users/qig/fproof/algebra_exercises_v4_11_0_cleaner_200inputnip.json"))
    process=[251,253,326,1559,1657]
    for key in process:
        if str(key) not in inp.keys():
            continue
        prompt=inp[str(key)]
        # with open(f"/ai4math/users/qig/fproof/algebra_exercises_prompt_{model}.jsonl", "a", encoding="utf-8") as file:
        #     file.write(json.dumps({"prompt":prompt},ensure_ascii=False)+'\n')
    # for prompt in inp:
        message = client.messages.create(
            max_tokens=1024,
            system=content,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        try:
            with open(f"/ai4math/users/qig/fproof/algebra_exercises_prompt_{model}_informal_res.jsonl", "a", encoding="utf-8") as file:
                file.write(json.dumps({"prompt":prompt, "response":message.content[0].text},ensure_ascii=False)+'\n')
            # lean_code_pattern = r'```lean\n(.*?)(?:\n```|$)' # Match to the end if not finished
            # matches = re.findall(lean_code_pattern, message.content[0].text, re.DOTALL)#find all code blocks en
            # new_output = '\n'.join(matches)
            with open(f"/ai4math/users/qig/fproof/{key}.lean", "w", encoding="utf-8") as file:
                file.write(message.content[0].text)
            # break
        except Exception as e:
            print(e)
            continue

        # with open(f"/ai4math/users/qig/fproof/algebra_exercises_prompt_{model}_res.out", "a", encoding="utf-8") as file:
        #     file.write(message)
        # break    

if __name__ == "__main__":
    main()
# from datasets import load_dataset
import json
# dataset = load_dataset("pkuAI4M/algebra_exercises_v4_11_0_cleaner", split='train')
# /ai4math/users/qig/fproof/starred-data-2.json
data=json.load(open("/ai4math/users/qig/fproof/starred-data-2.json"))
output = dict()
# with open("data.txt", "w") as f:
for example in data:
    # 打印每一行的内容
    # if not example["informal_proof"]:
    #     continue
    # f.write(f"{example["answer_id"]}\n## Input:\n\n**Informal theorem:**\n{example['informal_statement']}\n**Formal theorem:**\n{example['formal_statement']}\n**Informal proof:**\n{example['informal_proof']}\n\n## Output:\n\n**Formal proof:**\n{example['formal_proof']}\n\n--------------\n\n")
    formal_statement = example["formalProof"][:example["formalProof"].find(":= by")+len(":= by")].strip()
    output[example["id"]]=f"## Input:\n\n**Informal theorem:**\n{example['md']}\n**Formal theorem:**\n{formal_statement}\n**Informal proof:**\n{example['informalProof']}"
        # output.append(f"## Input:\n\n**Informal theorem:**\n{example['informal_statement']}\n**Formal theorem:**\n{example['formal_statement']}\n**Informal proof:**\n{example['informal_proof']}")
with open("/ai4math/users/qig/fproof/algebra_exercises_v4_11_0_cleaner_200input.json", "w") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)
from agentic_chunker import AgenticChunker
import markdown
import os
import pdb

file_path = "test_files/pronoun_dep.md"
# file_path = "test_files/multi_sentense_context.md"
api_key = os.environ.get('OPENAI_APIKEY')
with open(file_path, 'r', encoding='utf-8') as f:
    md_content = f.read()
text = markdown.markdown(md_content)
chunker = AgenticChunker(api_key=api_key, model="gpt-4o-mini")
chunks = chunker.agentic_chunking(text, '.')
[print(f"{chunk}\n****") for chunk in chunks]
pdb.set_trace()

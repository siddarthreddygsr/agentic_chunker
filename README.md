# AGENTIC CHUNKER

## Installation

```bash
pip install agentic-chunker
```

## Usage

```python
from agentic_chunker import AgenticChunker
import markdown
import os

file_path = "test_files/pronoun_dep.md"
api_key = os.environ.get('OPENAI_APIKEY')
with open(file_path, 'r', encoding='utf-8') as f:
    md_content = f.read()
text = markdown.markdown(md_content)
chunker = AgenticChunker(api_key=api_key, model="gpt-4o-mini")
chunks = chunker.agentic_chunking(text, '.')
```

## Dependencies
- openai

## Contributing
Contributions to AgenticChunker are welcome! Please make sure to follow the code style and conventions used in the project. If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the GPL-3.0 .
```


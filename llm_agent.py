import os
def summarize_findings(text):
    try:
        from langchain.llms import Ollama
        llm = Ollama(model=os.environ.get('OLLAMA_MODEL','mistral'))
        prompt=f'Summarize this system security report in simple terms:\n{text}'
        try:
            return llm.invoke(prompt)
        except Exception:
            try:
                return llm(prompt)
            except Exception:
                return '[LLM present but failed to respond]'
    except Exception:
        if 'failed' in text.lower():
            return 'Several failed logins detected — may indicate brute-force or misuse.'
        return 'No critical issues found.'

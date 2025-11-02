import pandas as pd

def parse_logs(file_path='sample_logs.txt'):
    logs=[]
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            for line in f:
                line=line.strip()
                if not line: continue
                entry={'raw':line}
                if 'Failed password' in line or 'Invalid user' in line:
                    entry['type']='alert'
                elif 'Accepted password' in line or 'session opened' in line:
                    entry['type']='login'
                else:
                    entry['type']='info'
                logs.append(entry)
    except FileNotFoundError:
        return pd.DataFrame(columns=['raw','type'])
    return pd.DataFrame(logs)

def detect_anomalies(df):
    if df.empty: return 'No logs available.'
    fails=df[df['type']=='alert']
    if len(fails)>=5:
        return 'Multiple failed login attempts detected — possible brute-force attack.'
    if len(fails)>=2:
        return 'Repeated failed logins detected — investigate source IPs.'
    return 'No major anomalies found.'

def summarize_logs_text(df,detection):
    lines=[f'Detection: {detection}','Top alerts:']
    alerts=df[df['type']=='alert']['raw'].tolist()[:5]
    for a in alerts: lines.append(a)
    if not alerts: lines.append('No alert logs found.')
    return '\n'.join(lines)

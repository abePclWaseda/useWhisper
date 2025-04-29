import pandas as pd

# CSVファイルのパス
csv_path = "/mnt/kiso-qnap3/hurigana-speech-corpus-aozora/train.csv"

# 出力するテキストファイルのパス
output_path = "/mnt/kiso-qnap3/yuabe/m1/useWhisper/data/train/text/targets.txt"

# 検索する audio_path
target_audio_path = "train/1y4eRgkEey/3VA5QzZL1f/D50JsbGwQA/9Y1hiCvbzIPfqYooLoME.mp3"

# CSV読み込み
df = pd.read_csv(csv_path)

# 該当する audio_path の target を抽出
matched_row = df[df["audio_path"] == target_audio_path]

# target列だけ取り出してテキストファイルに保存（1行1文で，10行分のみ）
matched_row["target"].to_csv(output_path, index=False, header=False)

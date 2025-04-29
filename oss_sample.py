import time
import whisper

input_file = "/mnt/kiso-qnap3/yuabe/m1/useWhisper/data/train/audio/short_clip.mp3"  # 音声データのファイルパス
output_file = "/mnt/kiso-qnap3/yuabe/m1/useWhisper/data/train/text/transcription.txt"  # 出力ファイル

model = whisper.load_model("medium")  # 使用するモデルを指定する

start_time = time.time()
result = model.transcribe(input_file, fp16=False)  # 音声データの文字起こし
end_time = time.time()
print(result["text"])  # 文字起こし結果の表示
print(f"実行時間: {end_time - start_time} seconds")

# 結果をファイルに保存
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result["text"] + "\n")

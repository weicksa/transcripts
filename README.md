# Optional Settings
it is recommended to add a huggingface directory and add <br>
```export HF_HOME="path/to/huggingface"``` <br>
to .bashrc

# Prereqeuisites
Both Bash scripts work out of the respective data folders, so they have to be moved/copied
there manually.

# Preprocessing
The default filetype of the audio files downloaded from ilias is .m4a.
The convert_m4a.sh shellscript automatically converts all *.m4a files in it's
directory to mp3 files and puts them in the folder data_mp3/ .

# Batch processing
The run_on_all.sh Shellscript takes all mp3 files in it's folder,
runs the transciption model on them and saves the transcription files
in a seperate folder as transcripts_results/{filename}.txt.

# Singular file processing
The run_whisper.py script can also be called manually on singular files.
To do this run: <br>
```python run_whisper.py {filename}.mp3 {save_folder} ``` <br>

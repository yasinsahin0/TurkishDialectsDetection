import pydub


def download_sound(self, sound_name, start_time, end_time, save_name):
    newAudio = AudioSegment.from_wav(sound_name)
    sound_piece = newAudio[start_time:end_time]
    sound_piece.export(self.splitter_path + save_name + ".wav", format="wav")


def file_list(self):
    direc = os.listdir(self.sound_file_path)
    wav_file_list = []
    for i in direc:
        if i != "split" and i[0] != ".":
            for files in os.listdir(self.sound_file_path + i):
                if files[0] != ".":
                    wav_file_list.append(self.sound_file_path + i + "/" + files)
    return wav_file_list


def split_sound(self, second):
    file_list = self.file_list()
    for sound_path in file_list:
        audio = AudioSegment.from_file(sound_path)
        seconds = int(audio.duration_seconds)
        listem = []
        count = 0
        for i in range(0, seconds, second):
            listem.append(i * 1000)
        for a in range(0, len(listem) - 1):
            count += 1
            self.split_count += 1
            self.download_sound(sound_path, listem[a], listem[a + 1],
                                sound_path.split("/")[2].split(".")[0] + "_" + str(count))


def create_ticket_data(self):
    sound_list = os.listdir(self.splitter_path)
    save_data_file = open(self.data_file_path, "a")
    save_data_file.write("file_name,class_name\n")
    for name in sound_list:
        if name[0] != ".":
            class_name = name.split("_")[1]
            file = open(self.data_file_path, "a")
            file.write(name + "," + class_name + "\n")
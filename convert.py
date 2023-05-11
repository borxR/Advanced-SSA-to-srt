

def convert_ssa_to_srt(ass_data):
    
    ssa_lines = f.splitlines()

    srt_lines = []
    current_line_number = 1

    for line in ssa_lines:
        line = line.strip()
        if line.startswith('Dialogue:'):
            fields = line.split(',')
            start_time = convert_ssa_time_to_seconds(fields[1])
            end_time = convert_ssa_time_to_seconds(fields[2])
            subtitle_text = ','.join(fields[9:]).replace('\\N', '\n')
            subtitle_lines = subtitle_text.split('\n')
            for subtitle_line in subtitle_lines:
                srt_lines.append(str(current_line_number))
                srt_lines.append("\n")
                srt_lines.append(f"{convert_seconds_to_srt_time(start_time)} --> {convert_seconds_to_srt_time(end_time)}")
                srt_lines.append("\n")
                srt_lines.append(subtitle_line)
                srt_lines.append("\n\n")
                current_line_number += 1
                
    return ''.join(srt_lines)

def convert_ssa_time_to_seconds(ssa_time):
    h, m, s = ssa_time.split(':')
    s, ms = s.split('.')
    return int(h)*3600 + int(m)*60 + int(s) + int(ms)/1000

def convert_seconds_to_srt_time(seconds):
    ms = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


convert_ssa_to_srt(ass_data)

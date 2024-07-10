def draw_progress_bar(progress=0, total=100, fill_char="#", empty_char="-", bar_len=20):
   
   percentage = (progress / total) * 100
 
   filled_len = int(bar_len * (progress / total))
 
   bar = fill_char * filled_len + empty_char * (bar_len - filled_len)
 
   progress_text = f"({percentage}% complete)"
 
   progress_bar = f"{bar} {progress_text}"
   return progress_bar
 
 
"""Inputs"""
 
progress_bar = draw_progress_bar(progress=50)
print(progress_bar)
 
progress_bar = draw_progress_bar(progress=10)
print(progress_bar)
 
progress_bar = draw_progress_bar(progress=30)
print(progress_bar)
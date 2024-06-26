from .sql_memory import build_memory
from .windows_memory import window_buffer_memory_builder

memory_map = { 
    "sql_buffer_memory": build_memory,
    "sql_windows_memory": window_buffer_memory_builder,
}
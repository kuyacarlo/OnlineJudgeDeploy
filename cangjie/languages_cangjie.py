# --- Cangjie language support (appended by Dockerfile.backend) ---
# Cangjie 1.0.5 (cjnative). cjc + runtime baked into the custom judge image at
# /opt/cangjie, exposed on PATH. Runtime libs on LD_LIBRARY_PATH.
# seccomp_rule = None (like Java) because the Cangjie runtime spawns threads and
# does its own mmap/futex/clone which strict allowlists (c_cpp/general) would kill.
_cangjie_env = [
    "CANGJIE_HOME=/opt/cangjie",
    "LD_LIBRARY_PATH=/opt/cangjie/runtime/lib/linux_x86_64_cjnative:/opt/cangjie/tools/lib",
] + default_env

_cangjie_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END
//TEMPLATE BEGIN
func add(a: Int64, b: Int64): Int64 {
    // code
    return a + b
}
//TEMPLATE END
//APPEND BEGIN
main() {
    println(add(1, 2))
}
//APPEND END""",
    "compile": {
        "src_name": "main.cj",
        "exe_name": "main",
        "max_cpu_time": 10000,
        "max_real_time": 20000,
        # cjc spawns worker threads; each reserves virtual address space. A
        # bounded address-space rlimit makes thread creation fail with
        # "Resource temporarily unavailable" -> SIGABRT. Java compile uses -1
        # for the same reason, so do the same here.
        "max_memory": -1,
        "compile_command": "/opt/cangjie/bin/cjc -O2 {src_path} -o {exe_path}",
        "env": _cangjie_env,
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": None,
        "env": _cangjie_env,
        "memory_limit_check_only": 1,
    },
}

languages.append(
    {"config": _cangjie_lang_config, "name": "Cangjie",
     "description": "Cangjie 1.0.5", "content_type": "text/x-cangjie"}
)

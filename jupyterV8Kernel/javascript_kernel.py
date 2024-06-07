from typing import Any, Dict, Optional

from ipykernel.kernelbase import Kernel
from py_mini_racer import MiniRacer


class JavaScriptKernel(Kernel):
    implementation = "JavaScriptKernel"
    implementation_version = "0.1"
    language = "javascript"
    language_info = {
        "name": "javascript",
        "mimetype": "application/javascript",
        "file_extension": ".js",
    }
    banner = "JavaScriptKernel"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.js_context = MiniRacer()
        self.language_version = self.js_context.v8_version

    def do_execute(
        self,
        code: str,
        silent: bool,
        store_history: bool = True,
        user_expressions: Optional[Dict] = None,
        allow_stdin: bool = False,
        *,
        cell_meta: Optional[Dict[str, Any]] = None,
        cell_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Execute the given code.
        """
        if not code.strip():
            return self._empty_response()
        try:
            result = self.js_context.eval(code)
            if not silent:
                self._send_output(result)
            return self._ok_response(result)
        except Exception as e:
            if not silent:
                self._send_error(str(e))
            return self._error_response(e)

    def _send_output(self, result: Any) -> None:
        stream_content = {"name": "stdout", "text": str(result)}
        self.send_response(self.iopub_socket, "stream", stream_content)

    def _send_error(self, error_message: str) -> None:
        stream_content = {"name": "stderr", "text": error_message}
        self.send_response(self.iopub_socket, "stream", stream_content)

    def _empty_response(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }

    def _ok_response(self, result: Any = None) -> Dict[str, Any]:
        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
            "result": result,
        }

    def _error_response(self, e: Exception) -> Dict[str, Any]:
        return {
            "status": "error",
            "execution_count": self.execution_count,
            "ename": str(type(e).__name__),
            "evalue": str(e),
            "traceback": [],
        }

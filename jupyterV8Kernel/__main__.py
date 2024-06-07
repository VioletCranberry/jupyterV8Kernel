from .javascript_kernel import JavaScriptKernel
from ipykernel.kernelapp import IPKernelApp

if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=JavaScriptKernel)

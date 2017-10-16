import sys
import os
import importlib
import requests
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from conf import settings

server_info = {}
for k,v in settings.PLUGIN_ITEMS.items():
    # 找到v字符串：src.plugins.nic.Nic，src.plugins.disk.Disk
    module_path,cls_name = v.rsplit('.',maxsplit=1)
    module = importlib.import_module(module_path)
    cls = getattr(module,cls_name)
    obj = cls()
    ret = obj.process()
    server_info[k] = ret

requests.post(
    url=settings.API,
    data=server_info
)
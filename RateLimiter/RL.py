from .ARL import Ratelimiter
from flask import request
from pathlib import Path
import sys
import os 

# __Filename=Path(sys.modules['__main__'].__file__).stem

# __root_dir = Path(__file__).resolve().parent.parent
# __FolderPath=__root_dir / "logs" / "API"




def RequiredRateLimiter(Cleaning=False,
                CooldownTime=20,AllowedFreq=8,CleaningFreq=80,ResetTime=8,Filename=None,FolderPath=None,FileType=".json"):
        # target_folder = FolderPath if FolderPath is not None else __FolderPath
        def Decorator(Func):
            def Wrapper(*args,**kwargs):
                Ip=request.remote_addr
                # Ip="12"

                CoolDown=Ratelimiter(IP_Adrs=Ip,*args,**kwargs)

                if CoolDown==1:
                    return Func(*args, **kwargs)
                else:
                    return f"Rate limit exceeded. Please wait {CoolDown} Secs.", 429    
            return Wrapper
        return Decorator
    

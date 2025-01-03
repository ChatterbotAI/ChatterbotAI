import os
import sys

# So that we can do `import chatterbotaiai in our tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import chatterbotaiai # noqa: E402

chatterbotai.api_base = os.getenv("FORG_API_BASE")  # type: ignore
chatterbotai.api_key = os.getenv("FORG_API_KEY")  # type: ignore

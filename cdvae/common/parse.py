from typing import Any, Dict, TextIO

import numpy as np
import json

from ase import Atoms


def atom_json_default(obj: Any) -> Dict:
    if hasattr(obj, "todict"):
        return obj.todict()
    if isinstance(obj, np.ndarray):
        return {"_np": True, "_d": obj.tolist()}
    raise TypeError


def atom_object_hook(dct: Dict) -> Any:
    if "_np" in dct:
        return np.array(dct["_d"])
    return dct


def atoms_json_dump(atoms: Atoms, file_obj: TextIO) -> None:
    return json.dump(atoms, file_obj, default=atom_json_default)


def atoms_json_dumps(atoms: Atoms) -> str:
    return json.dumps(atoms, default=atom_json_default)


def atoms_json_load(file_obj: TextIO) -> Atoms:
    return Atoms.fromdict(json.load(file_obj, object_hook=atom_object_hook))


def atoms_json_loads(s: str) -> Atoms:
    return json.loads(s, object_hook=atom_object_hook)

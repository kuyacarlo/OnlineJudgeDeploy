import sys
sys.path.insert(0, "/tmp")
from problem.models import Problem
from cangjie_templates import TEMPLATES

updated = 0
for pid, tpl in TEMPLATES.items():
    try:
        p = Problem.objects.get(_id=pid)
    except Problem.DoesNotExist:
        print("MISSING", pid)
        continue
    p.template = {"Cangjie": tpl}
    p.save(update_fields=["template"])
    updated += 1
    print("TEMPLATED", pid)
print("UPDATED", updated)

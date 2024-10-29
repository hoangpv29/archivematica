from django.db import migrations

JHOVE_TOOL_ID = "085d8690-93b7-4d31-84f7-2c5f4cbf6735"


def data_migration_up(apps, schema_editor):
    """Upgrade jhove tool version."""
    FPTool = apps.get_model("fpr", "FPTool")
    FPTool.objects.filter(uuid=JHOVE_TOOL_ID).update(version="1.32", slug="jhove-132")


def data_migration_down(apps, schema_editor):
    FPTool = apps.get_model("fpr", "FPTool")
    FPTool.objects.filter(uuid=JHOVE_TOOL_ID).update(version="1.26", slug="jhove-126")


class Migration(migrations.Migration):
    dependencies = [("fpr", "0044_remove_fits")]
    operations = [migrations.RunPython(data_migration_up, data_migration_down)]

from sqladmin import BaseView, expose


class BackupView(BaseView):
    name = "Backup"
    icon = "fa-solid fa-warehouse"

    @expose("/backup", methods=["GET"])
    async def backup(self, request):
        return await self.templates.TemplateResponse(
            request,
            "message.html",
            context={
                "view_name": self.name,
                "message": "backup was successfull"
            },
        )

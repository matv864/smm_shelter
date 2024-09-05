from datetime import date

from pydantic import BaseModel


class ReportComment_schema(BaseModel):
    date: date
    text: str
    type: "ReportType_schema"


class ReportType_schema(BaseModel):
    type: str

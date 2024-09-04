from typing import Optional
from uuid import UUID
from datetime import date

from fastapi import APIRouter, Request, status

from src.database import My_crud
from src.database.models import (
    Pet,
    News,
    ReportType,
    ReportComment,
    Transaction
)

from .schemas.pets import Pets_schema, Pet_schema
from .schemas.news import News_schema
from .schemas.reports import ReportComment_schema, ReportType_schema
from .schemas.transactions import Transaction_schema

main_pets_router = APIRouter()


# pets


@main_pets_router.get("/")
async def get_head(request: Request):
    return request.headers


@main_pets_router.get(
    "/pet/list",
    response_model=list[Pets_schema],
    status_code=status.HTTP_200_OK
)
async def get_all_pets(offset: int = 0, limit: int = 100):
    return await My_crud(Pet).get(
        offset=offset,
        limit=limit,
        multi=True
    )


@main_pets_router.get(
    "/pet/{pets_id}",
    response_model=Pet_schema,
    status_code=status.HTTP_200_OK
)
async def get_pet(pets_id):
    return await My_crud(Pet).get(filters=[Pet.id == pets_id])


# news


@main_pets_router.get(
    "/news",
    response_model=list[News_schema],
    status_code=status.HTTP_200_OK
)
async def get_news(
    start_date: Optional[date] = None,
    finish_date: Optional[date] = None,
    offset: int = 0,
    limit: int = 100
):
    filters = []
    if start_date:
        filters.append(News.date_of_publication >= start_date)
    if finish_date:
        filters.append(News.date_of_publication <= finish_date)

    return await My_crud(News).get(
        filters=filters,
        offset=offset,
        limit=limit,
        order_by=News.date_of_publication,
        multi=True
    )


# reports

@main_pets_router.get(
    "/report_comments",
    response_model=list[ReportComment_schema],
    status_code=status.HTTP_200_OK
)
async def get_report_comments(
    reportType_id: Optional[UUID] = None,
    start_date: Optional[date] = None,
    finish_date: Optional[date] = None
):
    filters = []
    if reportType_id:
        filters.append(ReportComment.type_id == reportType_id)
    if start_date:
        filters.append(ReportComment.date >= start_date)
    if finish_date:
        filters.append(ReportComment.date <= finish_date)

    return await My_crud(ReportComment).get(
        filters=filters,
        multi=True
    )


@main_pets_router.get(
    "/report_types",
    response_model=list[ReportType_schema],
    status_code=status.HTTP_200_OK
)
async def get_report_types():
    return await My_crud(ReportType).get(multi=True)


# transactions


@main_pets_router.get(
    "/transactions",
    response_model=list[Transaction_schema],
    status_code=status.HTTP_200_OK
)
async def get_transactions(
    start_date: Optional[date] = None,
    finish_date: Optional[date] = None
):
    filters = []
    if start_date:
        filters.append(Transaction.date_of_payment >= start_date)
    if finish_date:
        filters.append(Transaction.date_of_payment <= finish_date)

    return await My_crud(Transaction).get(
        filters=filters,
        multi=True
    )

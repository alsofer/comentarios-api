from api.models import Comment
from fastapi import APIRouter

router_comment = APIRouter(
    prefix="/comment",
    tags=["Comentários"]
)

@router_comment.post("/new", response_model=Comment, summary="Envia um novo comentário")
async def new_comment(comment: Comment):
    return comment
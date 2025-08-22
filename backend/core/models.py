from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description="the text of the option shown to the user")
    nextnode: Dict[str, Any] = Field(description="The next node content and its options")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="the main content of the story node")
    isEnding: bool = Field(description="Whether this node is and ending node")
    isWinningEnding: bool = Field(description="Whether this node is a winning ending node")
    options: Optional[StoryOptionLLM] = Field(default=None, description="The Options for this node")


class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story")
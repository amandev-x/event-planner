from fastapi import APIRouter, Body, status, HTTPException, Path 
from models.events import Event 
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = [
    {
    "id": 1,
    "title": "Python Web Development Workshop",
    "image": "https://example.com/images/python-workshop.jpg",
    "description": "Learn modern web development with Python and FastAPI. Build REST APIs, handle authentication, and deploy to production.",
    "tags": ["python", "fastapi", "workshop", "web-development", "backend"],
    "location": "Tech Hub Conference Room, San Francisco"
  },
  {
    "id": 2,
    "title": "AI & Machine Learning Meetup",
    "image": "https://example.com/images/ai-meetup.png",
    "description": "Join us for an evening of AI discussions, featuring talks on LLMs, computer vision, and practical ML applications in production.",
    "tags": ["ai", "machine-learning", "neural-networks", "deep-learning", "meetup"],
    "location": "Zoom"
  },
  {
    "id": 3,
    "title": "DevOps Best Practices Summit",
    "image": "https://example.com/images/devops-summit.jpg",
    "description": "A full-day summit covering CI/CD pipelines, containerization with Docker, Kubernetes orchestration, and cloud infrastructure automation.",
    "tags": ["devops", "kubernetes", "docker", "ci-cd", "cloud", "automation"],
    "location": "Convention Center, Austin TX"
  },
   {
    "id": 4,
    "title": "React & Frontend Development Bootcamp",
    "image": "https://example.com/images/react-bootcamp.png",
    "description": "Intensive 3-hour bootcamp on React fundamentals, hooks, state management, and building responsive UI components.",
    "tags": ["react", "javascript", "frontend", "ui", "bootcamp", "web"],
    "location": "Google Meet"
  },
  {
    "id": 5,
    "title": "Cybersecurity Awareness Conference",
    "image": "https://example.com/images/security-conf.jpg",
    "description": "Learn about the latest security threats, encryption techniques, secure coding practices, and how to protect your applications from vulnerabilities.",
    "tags": ["security", "cybersecurity", "encryption", "hacking", "privacy", "conference"],
    "location": "Microsoft Teams"
  }
]
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events():
    if not events:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event list is empty. Please add event to get it."
        )
    else:
        return events
    
@event_router.get("/{id}", response_model=Event) 
async def retrieve_event(id: int = Path(..., title="Event ID", gt=0, examples=1)):
    retrieve_event = []
    for event in events: 
        if event["id"] == id:
            retrieve_event.append(event)
            return event
    if not retrieve_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with supplied ID {id} not found"
        )
    
@event_router.get("/new")
async def create_new_event(body: Event = Body(...)):
    events.append(body)
    return {
        "Message": "Event Created Successfully."
    }

    
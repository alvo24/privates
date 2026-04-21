from apscheduler.schedulers.background import BackgroundScheduler

from app.schemas.models import PostDispatchRequest


class JobScheduler:
    def __init__(self, dispatcher_service) -> None:
        self.dispatcher_service = dispatcher_service
        self.scheduler = BackgroundScheduler(timezone="UTC")
        self.scheduler.start()

    def schedule_post(self, request: PostDispatchRequest) -> str:
        job = self.scheduler.add_job(
            self.dispatcher_service.publish_now,
            trigger="date",
            run_date=request.schedule_at,
            args=[request],
        )
        return job.id

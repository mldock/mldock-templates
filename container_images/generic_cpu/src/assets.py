"""
    CONTAINER ASSETS MANAGEMENT

    Provides class objects with methods to execute at certain parts of the container life-cycle, i.e. startup or cleanup, etc.
    In short we call them TrainingContainer and ServingContainer classes. Each provides everything your container needs, including
    environment, logger, etc.
    Since Serving Containers and Training Containers are unique in use-case and requirements, we recommend providing one for each workflow.
"""
from mldock.platform_helpers.mldock.configuration.container import (
    BaseServingContainer,
    BaseTrainingContainer,
)

# Training Container Assets Management
class TrainingContainer(BaseTrainingContainer):
    """
    Implements the base training container,
    allow a user to override/add/extend any training container setup logic
    """

    pass

# Serving Container Assets Management
class ServingContainer(BaseServingContainer):
    """
    Implements the base serving container,
    allow a user to override/add/extend any training container setup logic.
    """

    pass

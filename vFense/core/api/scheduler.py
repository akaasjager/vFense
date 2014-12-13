import simplejson as json

import logging
import logging.config
from vFense._constants import VFENSE_LOGGING_CONFIG

from vFense.core.agent.operations.store_agent_operations import (
    StoreAgentOperations
)
from vFense.core.agent.scheduler.search.search import RetrieveAgentJobs
from vFense.core.api.base import BaseHandler
from vFense.core.api._constants import ApiArguments
from vFense.core.decorators import (
    authenticated_request, convert_json_to_arguments, results_message
)
from vFense.core.operations.decorators import log_operation
from vFense.core.operations._admin_constants import AdminActions
from vFense.core.operations._constants import vFenseObjects
from vFense.core.permissions._constants import Permissions
from vFense.core.permissions.decorators import check_permissions
from vFense.core.results import ApiResults, ExternalApiResults
from vFense.core.scheduler._db_model import JobKeys
from vFense.core.scheduler.search.search import RetrieveJobs
from vFense.core.status_codes import GenericCodes, GenericFailureCodes
from vFense.core.tag.scheduler.search.search import RetrieveTagJobs
from vFense.core.user._db_model import UserKeys
from vFense.core.user.manager import UserManager
from vFense.plugins.patching.operations.store_operations import (
    StorePatchingOperation
)


logging.config.fileConfig(VFENSE_LOGGING_CONFIG)
logger = logging.getLogger('vfense_api')


class AgentJobsHandler(BaseHandler):
    @authenticated_request
    @check_permissions(Permissions.READ)
    def get(self, agent_id):
        count = int(self.get_argument(ApiArguments.COUNT, 30))
        offset = int(self.get_argument(ApiArguments.OFFSET, 0))
        query = self.get_argument(ApiArguments.QUERY, None)
        operation = self.get_argument(ApiArguments.OPERATION, None)
        trigger = self.get_argument('trigger', None)
        timezone = self.get_argument('timezone', None)
        sort = self.get_argument(ApiArguments.SORT, 'desc')
        sort_by = self.get_argument(ApiArguments.SORT_BY, JobKeys.NextRunTime)
        output = self.get_argument(ApiArguments.OUTPUT, 'json')

        search = (
            RetrieveAgentJobs(
                agent_id=agent_id, count=count, offset=offset,
                sort=sort, sort_key=sort_by
            )
        )
        if not operation and not trigger and not query and not timezone:
            results = self.get_all_jobs(search)

        elif query and not operation and not trigger and not timezone:
            results = self.get_all_jobs_by_name(search, query)

        elif operation and not trigger and not query and not timezone:
            results = self.get_all_jobs_by_operation(search, operation)

        elif trigger and not operation and not query and not timezone:
            results = self.get_all_jobs_by_trigger(search, trigger)

        elif timezone and not operation and not query and not trigger:
            results = self.get_all_jobs_by_timezone(search, timezone)

        elif query and trigger and not operation and not timezone:
            results = self.get_all_jobs_by_name_and_trigger(
                search, query, trigger
            )

        elif operation and trigger and not query and not timezone:
            results = self.get_all_jobs_by_operation_and_trigger(
                search, operation, trigger
            )

        elif query and operation and trigger:
            results = (
                self.get_all_jobs_by_name_and_trigger_and_operation(
                    search, query, trigger, operation
                )
            )

        self.set_status(results.http_status_code)
        self.modified_output(results, output, 'jobs')

    @results_message
    def get_all_jobs(self, search):
        results = search.all()
        return results

    @results_message
    def get_all_jobs_by_name(self, search, name):
        results = search.by_name(name)
        return results

    @results_message
    def get_all_jobs_by_trigger(self, search, trigger):
        results = search.by_trigger(trigger)
        return results

    @results_message
    def get_all_jobs_by_operation(self, search, operation):
        results = search.by_operation(operation)
        return results

    @results_message
    def get_all_jobs_by_timezone(self, search, timezone):
        results = search.by_timezone(timezone)
        return results

    @results_message
    def get_all_jobs_by_name_and_trigger(self, search, name, trigger):
        results = search.by_name_and_trigger(name, trigger)
        return results

    @results_message
    def get_all_jobs_by_operation_and_trigger(self, search, operation,
                                              trigger):
        results = search.by_operation_and_trigger(operation, trigger)
        return results

    @results_message
    def get_all_jobs_by_name_and_trigger_and_operation(self, search, name,
                                                       trigger, operation):
        results = (
            search.by_name_and_trigger_and_operation(
                name, trigger, operation
            )
        )
        return results

class TagJobsHandler(BaseHandler):
    @authenticated_request
    @check_permissions(Permissions.READ)
    def get(self, tag_id):
        count = int(self.get_argument(ApiArguments.COUNT, 30))
        offset = int(self.get_argument(ApiArguments.OFFSET, 0))
        query = self.get_argument(ApiArguments.QUERY, None)
        operation = self.get_argument(ApiArguments.OPERATION, None)
        trigger = self.get_argument('trigger', None)
        timezone = self.get_argument('timezone', None)
        sort = self.get_argument(ApiArguments.SORT, 'desc')
        sort_by = self.get_argument(ApiArguments.SORT_BY, JobKeys.NextRunTime)
        output = self.get_argument(ApiArguments.OUTPUT, 'json')

        search = (
            RetrieveTagJobs(
                tag_id=tag_id, count=count, offset=offset,
                sort=sort, sort_key=sort_by
            )
        )
        if not operation and not trigger and not query and not timezone:
            results = self.get_all_jobs(search)

        elif query and not operation and not trigger and not timezone:
            results = self.get_all_jobs_by_name(search, query)

        elif operation and not trigger and not query and not timezone:
            results = self.get_all_jobs_by_operation(search, operation)

        elif trigger and not operation and not query and not timezone:
            results = self.get_all_jobs_by_trigger(search, trigger)

        elif timezone and not operation and not query and not trigger:
            results = self.get_all_jobs_by_timezone(search, timezone)

        elif query and trigger and not operation and not timezone:
            results = self.get_all_jobs_by_name_and_trigger(
                search, query, trigger
            )

        elif operation and trigger and not query and not timezone:
            results = self.get_all_jobs_by_operation_and_trigger(
                search, operation, trigger
            )

        elif query and operation and trigger:
            results = (
                self.get_all_jobs_by_name_and_trigger_and_operation(
                    search, query, trigger, operation
                )
            )

        self.set_status(results.http_status_code)
        self.modified_output(results, output, 'jobs')

    @results_message
    def get_all_jobs(self, search):
        results = search.all()
        return results

    @results_message
    def get_all_jobs_by_name(self, search, name):
        results = search.by_name(name)
        return results

    @results_message
    def get_all_jobs_by_trigger(self, search, trigger):
        results = search.by_trigger(trigger)
        return results

    @results_message
    def get_all_jobs_by_operation(self, search, operation):
        results = search.by_operation(operation)
        return results

    @results_message
    def get_all_jobs_by_timezone(self, search, timezone):
        results = search.by_timezone(timezone)
        return results

    @results_message
    def get_all_jobs_by_name_and_trigger(self, search, name, trigger):
        results = search.by_name_and_trigger(name, trigger)
        return results

    @results_message
    def get_all_jobs_by_operation_and_trigger(self, search, operation,
                                              trigger):
        results = search.by_operation_and_trigger(operation, trigger)
        return results

    @results_message
    def get_all_jobs_by_name_and_trigger_and_operation(self, search, name,
                                                       trigger, operation):
        results = (
            search.by_name_and_trigger_and_operation(
                name, trigger, operation
            )
        )
        return results

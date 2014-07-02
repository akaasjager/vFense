import simplejson as json

import logging
import logging.config
from vFense import VFENSE_LOGGING_CONFIG

from vFense.core.api.base import BaseHandler
from vFense.core.api._constants import (
    ApiArguments, ApiValues
)
from vFense.core.permissions._constants import Permissions
from vFense.core.permissions.decorators import check_permissions
from vFense.core.operations.decorators import log_operation
from vFense.core.operations._admin_constants import AdminActions
from vFense.core.operations._constants import vFenseObjects
from vFense.core.scheduler._db_model import JobKeys
from vFense.core.user._db_model import UserKeys
from vFense.core.user.manager import UserManager
from vFense.core.scheduler.search.search import RetrieveJobs
from vFense.result.error_messages import GenericResults
from vFense.result.results import Results
from pytz import all_timezones

from vFense.plugins.patching.operations.store_operations import (
    StorePatchingOperation
)
from vFense.core.agent.operations.store_agent_operations import (
    StoreAgentOperations
)

from vFense.core.decorators import (
    authenticated_request, convert_json_to_arguments, results_message
)
from vFense.result._constants import ApiResultKeys
from vFense.result.status_codes import (
    GenericCodes, GenericFailureCodes
)

logging.config.fileConfig(VFENSE_LOGGING_CONFIG)
logger = logging.getLogger('rvapi')


class TimeZonesHandler(BaseHandler):
    @authenticated_request
    @check_permissions(Permissions.READ)
    def get(self):
        results = self.get_timezones()
        self.set_header('Content-Type', 'application/json')
        self.set_status(results['http_status'])
        self.write(json.dumps(results, indent=4))
        self.write(json.dumps(results, indent=4))

    @results_message
    def get_timezones(self):
        data = all_timezones
        results = (
            {
                ApiResultKeys.DATA: data,
                ApiResultKeys.GENERIC_STATUS_CODE: GenericCodes.InformationRetrieved
            }
        )
        return results

class JobHandler(BaseHandler):
    @authenticated_request
    @check_permissions(Permissions.READ)
    def get(self, job_id):
        username = self.get_current_user()
        active_view = (
            UserManager(username).get_attribute(UserKeys.CurrentView)
        )
        search = RetrieveJobs(active_view)
        results = self.get_job_by_id(search, job_id)
        self.set_header('Content-Type', 'application/json')
        self.set_status(results['http_status'])
        self.write(json.dumps(results, indent=4))
        self.write(json.dumps(results, indent=4))

    @results_message
    def get_job_by_id(self, search, job_id):
        results = search.by_id(job_id)
        return results


class JobsHandler(BaseHandler):
    @authenticated_request
    @check_permissions(Permissions.READ)
    def get(self):
        username = self.get_current_user()
        user = UserManager(username)
        active_view = user.get_attribute(UserKeys.CurrentView)
        count = int(self.get_argument('count', 30))
        offset = int(self.get_argument('offset', 0))
        query = self.get_argument('query', None)
        operation = self.get_argument('operation', None)
        trigger = self.get_argument('trigger', None)
        timezone = self.get_argument('timezone', None)
        sort = self.get_argument('sort', 'desc')
        sort_by = self.get_argument('sort_by', JobKeys.NextRunTime)

        search = (
            RetrieveJobs(active_view, count, offset, sort, sort_by)
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

        self.set_status(results['http_status'])
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(results, indent=4))

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


class AgentJobsHandler(BaseHandler):
    @authenticated_request
    @check_permissions(Permissions.READ)
    def get(self, agent_id):
        count = int(self.get_argument('count', 30))
        offset = int(self.get_argument('offset', 0))
        query = self.get_argument('query', None)
        operation = self.get_argument('operation', None)
        trigger = self.get_argument('trigger', None)
        timezone = self.get_argument('timezone', None)
        sort = self.get_argument('sort', 'desc')
        sort_by = self.get_argument('sort_by', JobKeys.NextRunTime)

        search = (
            RetrieveJobs(agent_id, count, offset, sort, sort_by)
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

        self.set_status(results['http_status'])
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(results, indent=4))

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
        count = int(self.get_argument('count', 30))
        offset = int(self.get_argument('offset', 0))
        query = self.get_argument('query', None)
        operation = self.get_argument('operation', None)
        trigger = self.get_argument('trigger', None)
        timezone = self.get_argument('timezone', None)
        sort = self.get_argument('sort', 'desc')
        sort_by = self.get_argument('sort_by', JobKeys.NextRunTime)

        search = (
            RetrieveJobs(tag_id, count, offset, sort, sort_by)
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

        self.set_status(results['http_status'])
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(results, indent=4))

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

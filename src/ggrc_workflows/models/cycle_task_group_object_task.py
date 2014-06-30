# Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: dan@reciprocitylabs.com
# Maintained By: dan@reciprocitylabs.com


from ggrc import db
from ggrc.models.mixins import (
    Base, Titled, Described, Timeboxed, Stateful, WithContact
    )


class CycleTaskGroupObjectTask(
    WithContact, Stateful, Timeboxed, Described, Titled, Base, db.Model):
  __tablename__ = 'cycle_task_group_object_tasks'
  _title_uniqueness = False

  VALID_STATES = (None, 'InProgress', 'Assigned', 'Finished', 'Declined', 'Verified')

  cycle_task_group_object_id = db.Column(
      db.Integer, db.ForeignKey('cycle_task_group_objects.id'), nullable=False)
  task_group_task_id = db.Column(
      db.Integer, db.ForeignKey('task_group_tasks.id'), nullable=False)
  task_group_task = db.relationship(
    "TaskGroupTask",
    foreign_keys="CycleTaskGroupObjectTask.task_group_task_id"
    )
  sort_index = db.Column(
      db.String(length=250), nullable=False)

  _publish_attrs = [
      'cycle_task_group_object',
      'task_group_task',
      'cycle_task_entries',
      'sort_index',
      ]

import TaskForm from "../organisms/TaskForm"
import TaskList from "../organisms/TaskList"

const TaskManagementTemplate = ({
  task,
  setTask,
  isEditing,
  handleSubmit,
  handleCancel,
  ongoingTasks,
  completedTasks,
  onEdit,
  onDelete,
  onToggleComplete,
  loading,
  error
}) => {
  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="font-poppins text-4xl font-normal text-center mb-6">Task Management</h1>

      {loading && <p className="text-center text-blue-500">Loading tasks...</p>}
      {error && <p className="text-center text-red-500">{error}</p>}

      <TaskForm
        task={task}
        setTask={setTask}
        isEditing={isEditing}
        handleSubmit={handleSubmit}
        handleCancel={handleCancel}
      />

      <TaskList
        title="Ongoing Task"
        tasks={ongoingTasks}
        onEdit={onEdit}
        onDelete={onDelete}
        onToggleComplete={onToggleComplete}
      />

      <TaskList
        title="Completed Task"
        tasks={completedTasks}
        onEdit={onEdit}
        onDelete={onDelete}
        onToggleComplete={onToggleComplete}
      />
    </div>
  )
}

export default TaskManagementTemplate

import TaskItem from "../molecules/TaskItem"

const TaskList = ({ title, tasks, onEdit, onDelete, onToggleComplete }) => {
  return (
    <div className="mb-6">
      <h2 className="font-bold mb-2">{title}</h2>
      {tasks.length === 0 ? (
        <p className="text-gray-500 text-sm">No tasks available</p>
      ) : (
        tasks.map((task) => (
          <TaskItem key={task.id} task={task} onEdit={onEdit} onDelete={onDelete} onToggleComplete={onToggleComplete} />
        ))
      )}
    </div>
  )
}

export default TaskList

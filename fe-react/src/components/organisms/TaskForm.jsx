"use client"
import FormField from "../molecules/FormField"
import Button from "../atoms/Button"

const TaskForm = ({ task, setTask, isEditing, handleSubmit, handleCancel }) => {
  const handleChange = (e) => {
    setTask({ ...task, title: e.target.value })
  }

  return (
    <form onSubmit={handleSubmit} className="mb-6">
      <FormField
        
        label="Title"
        placeholder="Enter task title"
        value={task.title}
        onChange={handleChange}
        name="title"
        required
      />
      <div className="flex justify-center space-x-2">
        {isEditing ? (
          <>
            <Button type="submit" variant="secondary">
              Update Task
            </Button>
            <Button type="button" variant="danger" onClick={handleCancel}>
              Cancel
            </Button>
          </>
        ) : (
          <Button type="submit" variant="primary">
            Add Task
          </Button>
        )}
      </div>
    </form>
  )
}

export default TaskForm

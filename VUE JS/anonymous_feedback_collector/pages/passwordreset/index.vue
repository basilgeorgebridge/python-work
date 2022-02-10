<template>
  <v-form
    ref="form"
    v-model="form"
    lazy-validation
  >
    <v-text-field
      v-model="password"
      :counter="20"
      :rules="[(password === passwordCheck) || 'Passwords must match', ...passwordRules]"
      :type="'password'"
      label="Password"
      required
    ></v-text-field>
    <v-text-field
      v-model="passwordCheck"
      :rules="[(password === passwordCheck) || 'Passwords must match', ...passwordRules]"
      :counter="20"
      :type="'password'"
      label="Password"
      required
    ></v-text-field>
    <v-btn
      color="indigo lighten-1"
      class="mr-4"
      @click="validate"
    >
      {{ buttonTitle }}
    </v-btn>
  </v-form>
</template>

<script>
export default {
  name: 'changePasswordForm',
  data: () => ({
    passwordRules: [
      v => !!v || 'Password is required',
      v => (v && v.length <= 20) || 'Password must be less than 20 characters',
    ]
  }),
  props: {
    form: {
      required: true,
    },
    buttonTitle: {
      required: true
    }
  },
  mounted () {
  this.form = false
    },
  methods: {
    validate () {
      if (this.$refs.form) {
        this.form.finish = true
        this.$emit('update:form', this.form)
      }
    }
  }
}
</script>
